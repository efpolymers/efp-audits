// paginate-and-export.js
const puppeteer = require('puppeteer');
const fs = require('fs');
const path = require('path');

const CHROME_PATH = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';

// ---- tunables ----
const MAX_PAGE_HEIGHT = 1115;      // content-area height budget per page (matches your original)
const MIN_ROWS_BEFORE_SPLIT = 3;   // fewer fitting data rows than this => move whole table instead of splitting
const MAX_ITERATIONS = 40;         // safety cap for the fixed-point loop
const ZOOM = process.env.PDF_ZOOM || '0.94';

function launchOpts() {
  const o = { headless: 'new' };
  if (fs.existsSync(CHROME_PATH)) o.executablePath = CHROME_PATH;
  return o;
}

async function withAuthBypass(page) {
  await page.evaluateOnNewDocument(() => {
    localStorage.setItem('reports_auth_expiry', (Date.now() + 2 * 60 * 60 * 1000).toString());
  });
}

async function injectPrintStyles(page) {
  await page.addStyleTag({
    content: `
      @page { margin: 0px !important; }
      body { background: transparent !important; zoom: ${ZOOM} !important; }
      .page { margin: 0px auto 0px auto !important; box-shadow: none !important; }
    `
  });
}

/**
 * The whole layout algorithm, executed inside the browser context.
 * Runs entirely synchronously against the live DOM so getBoundingClientRect()
 * always reflects the current, mutated layout.
 */
function runLayoutEngine(MAX_PAGE_HEIGHT, MIN_ROWS_BEFORE_SPLIT, MAX_ITERATIONS, docTitle) {
  const log = [];

  // ---------- generic helpers ----------
  function relBottom(el, pageEl) {
    return el.getBoundingClientRect().bottom - pageEl.getBoundingClientRect().top;
  }
  function contentChildren(pageEl) {
    return Array.from(pageEl.children).filter(
      c => !c.classList.contains('letterhead') && !c.classList.contains('doc-footer')
    );
  }
  function makePage() {
    const p = document.createElement('div');
    p.className = 'page';
    const lh = document.createElement('img');
    lh.src = 'letterhead.png';
    lh.alt = 'Letterhead';
    lh.className = 'letterhead';
    p.appendChild(lh);
    document.body.appendChild(p); // must be attached to measure
    return p;
  }
  function removeFooters(pageEl) {
    Array.from(pageEl.querySelectorAll(':scope > .doc-footer')).forEach(f => f.remove());
  }
  // Insert `nodes` (in order) right after the letterhead, before whatever is already there.
  function insertAfterLetterhead(pageEl, nodes) {
    const letterhead = pageEl.querySelector('.letterhead');
    const refNode = letterhead ? letterhead.nextSibling : pageEl.firstChild;
    nodes.forEach(n => pageEl.insertBefore(n, refNode)); // auto-detaches n from old parent
  }

  // ---------- Step 0: flatten into blocks, split off the cover ----------
  const originalPages = Array.from(document.querySelectorAll('.page'));
  let coverPage = null;
  const blocks = [];

  originalPages.forEach(p => {
    if (p.classList.contains('cover')) {
      coverPage = p.cloneNode(true);
      removeFooters(coverPage);
      p.remove();
      return;
    }
    contentChildren(p).forEach(k => {
      const clone = k.cloneNode(true);
      if (clone.classList && clone.classList.contains('eyebrow')) {
        clone.setAttribute('data-section-start', '1');
        log.push(`Found section start: ${clone.textContent.substring(0, 30)}`);
      }
      blocks.push(clone);
    });
    p.remove();
  });

  document.body.innerHTML = ''; // clean slate; we rebuild everything below

  // ---------- Pass 1: force a fresh page at every section (.eyebrow) ----------
  let pages = [];
  let current = makePage();
  pages.push(current);

  blocks.forEach(b => {
    const isSectionStart = b.getAttribute && b.getAttribute('data-section-start') === '1';
    if (isSectionStart && contentChildren(current).length > 0) {
      current = makePage();
      pages.push(current);
    }
    current.appendChild(b);
  });

  log.push(`Pass 1: ${blocks.length} blocks -> ${pages.length} section-aligned pages.`);

  function getNextPageForOverflow(pageIndex) {
    let nextPage = pages[pageIndex + 1];
    if (!nextPage) {
      nextPage = makePage();
      pages.splice(pageIndex + 1, 0, nextPage);
    } else {
      const nextKids = contentChildren(nextPage);
      if (nextKids.length > 0 && nextKids[0].getAttribute && nextKids[0].getAttribute('data-section-start') === '1') {
        nextPage = makePage();
        pages.splice(pageIndex + 1, 0, nextPage);
      }
    }
    return nextPage;
  }

  // ---------- Pass 2: fix overflow, then fix underflow, iterate to fixed point ----------
  function handleTableOverflow(table, pageEl, pageIndex) {
    const rows = Array.from(table.querySelectorAll('tr'));
    let splitIdx = -1;
    for (let i = 0; i < rows.length; i++) {
      if (relBottom(rows[i], pageEl) > MAX_PAGE_HEIGHT) { splitIdx = i; break; }
    }
    if (splitIdx === -1) return false; // shouldn't happen if caller already confirmed overflow

    const headerRowCount = rows.filter(r => r.querySelector('th')).length;
    const dataRowsFitting = splitIdx - headerRowCount;

    let nextPage = getNextPageForOverflow(pageIndex);

    if (dataRowsFitting < MIN_ROWS_BEFORE_SPLIT) {
      // Too few rows fit to be worth splitting here -> move the whole table forward.
      const moveNodes = [table];
      const prev = table.previousElementSibling;
      if (prev && /^(H2|H3|H4|H5)$/.test(prev.tagName)) moveNodes.unshift(prev);
      insertAfterLetterhead(nextPage, moveNodes);
      log.push(`Page ${pageIndex + 1}: only ${dataRowsFitting} data row(s) fit — moved whole table${moveNodes.length > 1 ? ' + heading' : ''} to next page.`);
    } else {
      // Split: keep rows [0, splitIdx) here, clone header(s) + remaining rows into a new table next page.
      const nextTable = table.cloneNode(false);
      rows.filter(r => r.querySelector('th')).forEach(hr => nextTable.appendChild(hr.cloneNode(true)));
      for (let i = splitIdx; i < rows.length; i++) nextTable.appendChild(rows[i]); // moves node
      insertAfterLetterhead(nextPage, [nextTable]);
      log.push(`Page ${pageIndex + 1}: split table at row ${splitIdx} — kept ${dataRowsFitting} data row(s), moved ${rows.length - splitIdx} to next page.`);
    }
    return true;
  }

  function handleGenericOverflow(el, pageEl, pageIndex) {
    let nextPage = getNextPageForOverflow(pageIndex);
    const moveNodes = [el];
    const prev = el.previousElementSibling;
    if (prev && /^(H2|H3|H4|H5)$/.test(prev.tagName)) moveNodes.unshift(prev);
    insertAfterLetterhead(nextPage, moveNodes);
    log.push(`Page ${pageIndex + 1}: moved overflowing <${el.tagName}>${moveNodes.length > 1 ? ' + heading' : ''} to next page.`);
    return true;
  }

  function tryPullBack(pageIndex) {
    const pageEl = pages[pageIndex];
    const nextPage = pages[pageIndex + 1];
    if (!nextPage) return false;
    const nextKids = contentChildren(nextPage);
    if (nextKids.length === 0) return false;

    const first = nextKids[0];
    if (first.getAttribute && first.getAttribute('data-section-start') === '1') return false; // never pull a new section back
    const isHeading = /^(H2|H3|H4|H5)$/.test(first.tagName);
    if (isHeading && nextKids.length > 1) return false; // don't orphan a heading from its content

    pageEl.appendChild(first); // tentative move
    const fits = relBottom(first, pageEl) <= MAX_PAGE_HEIGHT;
    if (!fits) {
      insertAfterLetterhead(nextPage, [first]); // revert
      return false;
    }
    log.push(`Pulled a <${first.tagName}> back from page ${pageIndex + 2} to page ${pageIndex + 1}.`);
    return true;
  }

  function removeEmptyPages() {
    for (let i = pages.length - 1; i >= 0; i--) {
      if (contentChildren(pages[i]).length === 0) {
        pages[i].remove();
        pages.splice(i, 1);
        log.push(`Removed now-empty page at position ${i + 1}.`);
      }
    }
  }

  let iteration = 0;
  let changed = true;
  while (changed && iteration < MAX_ITERATIONS) {
    changed = false;
    iteration++;

    // -- fix overflow --
    for (let pi = 0; pi < pages.length; pi++) {
      const pageEl = pages[pi];
      const kids = contentChildren(pageEl);
      let overflowEl = null;

      for (const k of kids) {
        if (k.hasAttribute('data-unmovable')) continue;
        if (relBottom(k, pageEl) > MAX_PAGE_HEIGHT) { overflowEl = k; break; }
      }
      if (!overflowEl) continue;

      const isFirst = kids.indexOf(overflowEl) === 0;
      if (isFirst && overflowEl.tagName !== 'TABLE') {
        // Taller than a full page and can't be split further at this granularity — accept the bleed.
        overflowEl.setAttribute('data-unmovable', '1');
        log.push(`Page ${pi + 1}: <${overflowEl.tagName}> is taller than one page and can't be split — left as-is.`);
        continue;
      }

      if (overflowEl.tagName === 'TABLE') {
        if (handleTableOverflow(overflowEl, pageEl, pi)) changed = true;
      } else {
        if (handleGenericOverflow(overflowEl, pageEl, pi)) changed = true;
      }
    }

    // -- fix underflow (pull content back where there's slack) --
    for (let pi = 0; pi < pages.length - 1; pi++) {
      let pulled = tryPullBack(pi);
      while (pulled) { changed = true; pulled = tryPullBack(pi); }
    }

    removeEmptyPages();
  }

  log.push(`Pass 2 stabilized after ${iteration} iteration(s). Final page count: ${pages.length}.`);
  if (iteration >= MAX_ITERATIONS) log.push(`WARNING: hit MAX_ITERATIONS cap — output may not be fully settled.`);

  // ---------- Step 3: footers, numbering, cleanup ----------
  const finalOrder = [];
  if (coverPage) finalOrder.push(coverPage);
  finalOrder.push(...pages);

  document.body.innerHTML = '';
  finalOrder.forEach((p, idx) => {
    removeFooters(p);
    p.querySelectorAll('[data-section-start],[data-unmovable]').forEach(n => {
      n.removeAttribute('data-section-start');
      n.removeAttribute('data-unmovable');
    });
    const footer = document.createElement('div');
    footer.className = 'doc-footer';
    const t = document.createElement('span'); t.textContent = docTitle;
    const n = document.createElement('span'); n.textContent = `Page ${idx + 1}`;
    footer.appendChild(t); footer.appendChild(n);
    p.appendChild(footer);
    document.body.appendChild(p);
  });

  // strip the injected zoom style before we serialize
  document.querySelectorAll('style').forEach(s => {
    if (s.textContent.includes('zoom:')) s.remove();
  });

  return { html: document.documentElement.outerHTML, log };
}

async function paginateAndExport(inputPath, outHtmlPath, outPdfPath, docTitle) {
  // --- phase A: run the layout engine on the original file ---
  const browser1 = await puppeteer.launch(launchOpts());
  const page1 = await browser1.newPage();
  await withAuthBypass(page1);
  await page1.goto(`file://${inputPath}`, { waitUntil: 'networkidle0' });
  await injectPrintStyles(page1);

  const { html, log } = await page1.evaluate(
    runLayoutEngine,
    MAX_PAGE_HEIGHT,
    MIN_ROWS_BEFORE_SPLIT,
    MAX_ITERATIONS,
    docTitle
  );
  await browser1.close();

  console.log(log.join('\n'));
  fs.writeFileSync(outHtmlPath, '<!DOCTYPE html>\n' + html);
  console.log(`✅ Paginated HTML written: ${outHtmlPath}`);

  // --- phase B: reopen the FINAL file fresh (so relative asset paths resolve cleanly) and export PDF ---
  const browser2 = await puppeteer.launch(launchOpts());
  const page2 = await browser2.newPage();
  await withAuthBypass(page2);
  await page2.goto(`file://${outHtmlPath}`, { waitUntil: 'networkidle0' });
  await injectPrintStyles(page2);

  await page2.pdf({
    path: outPdfPath,
    format: 'A4',
    printBackground: true,
    margin: { top: '0px', right: '0px', bottom: '0px', left: '0px' }
  });
  await browser2.close();
  console.log(`✅ PDF generated: ${outPdfPath}`);
}

async function main() {
  const targetFile = process.argv[2] || '00-overall-analysis.html';
  const inputPath = path.join(__dirname, targetFile);
  if (!fs.existsSync(inputPath)) {
    console.error(`❌ File not found: ${inputPath}`);
    process.exit(1);
  }

  let docTitle = 'EF Polymer Report';
  if (targetFile.includes('overall')) docTitle = 'Overall Analysis · EF Polymer · v2.0';
  else if (targetFile.includes('ceo')) docTitle = 'CEO Office · EF Polymer';

  const outHtmlPath = path.join(__dirname, targetFile.replace('.html', '-autopaged.html'));
  const outPdfPath = path.join(__dirname, targetFile.replace('.html', '-autopaged.pdf'));

  console.log(`🚀 Starting layout + export for ${targetFile}...`);
  await paginateAndExport(inputPath, outHtmlPath, outPdfPath, docTitle);
}

main();