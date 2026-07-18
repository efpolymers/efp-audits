const puppeteer = require('puppeteer');
const path = require('path');

(async () => {
  const browser = await puppeteer.launch({ headless: 'new' });
  const page = await browser.newPage();
  
  await page.evaluateOnNewDocument(() => {
    localStorage.setItem('reports_auth_expiry', (Date.now() + 2 * 60 * 60 * 1000).toString());
  });

  const filePath = path.join(__dirname, '00-overall-analysis.html');
  await page.goto(`file://${filePath}`, { waitUntil: 'networkidle0' });

  // Inject styles to match generate-pdf.js
  await page.addStyleTag({
    content: `
      @page { margin: 0px !important; }
      body { background: transparent !important; zoom: 0.94 !important; }
      .page { margin: 0px auto 0px auto !important; box-shadow: none !important; }
    `
  });

  const heuristics = await page.evaluate(() => {
    const pages = document.querySelectorAll('.page');
    const MAX_PAGE_HEIGHT = 1120;
    let results = [];

    pages.forEach((page, index) => {
      const pageRect = page.getBoundingClientRect();
      const elements = Array.from(page.children);
      
      let overflowStartElement = null;
      let overflowBottom = 0;

      for (let i = 0; i < elements.length; i++) {
        const el = elements[i];
        const rect = el.getBoundingClientRect();
        const relativeBottom = rect.bottom - pageRect.top;
        
        if (relativeBottom > MAX_PAGE_HEIGHT && !overflowStartElement) {
          overflowStartElement = el;
          overflowBottom = relativeBottom;
          break;
        }
      }

      if (overflowStartElement) {
        let headingCandidate = null;
        for (let i = elements.indexOf(overflowStartElement); i >= 0; i--) {
          if (['H1', 'H2', 'H3', 'H4', 'H5'].includes(elements[i].tagName)) {
            headingCandidate = elements[i].textContent.trim();
            break;
          }
        }

        let tableCutInfo = null;
        if (overflowStartElement.tagName === 'TABLE' || overflowStartElement.querySelector('table')) {
          const table = overflowStartElement.tagName === 'TABLE' ? overflowStartElement : overflowStartElement.querySelector('table');
          const rows = Array.from(table.querySelectorAll('tr'));
          for (let r = 0; r < rows.length; r++) {
            const rowRect = rows[r].getBoundingClientRect();
            const rowBottom = rowRect.bottom - pageRect.top;
            if (rowBottom > MAX_PAGE_HEIGHT) {
              tableCutInfo = {
                rowToCutAfterIndex: r - 1,
                totalRows: rows.length,
                cutAfterRowContent: rows[r-1] ? rows[r-1].textContent.trim().replace(/\s+/g, ' ').substring(0, 100) : 'none',
                overflowRowContent: rows[r] ? rows[r].textContent.trim().replace(/\s+/g, ' ').substring(0, 100) : 'none'
              };
              break;
            }
          }
        }

        results.push({
          pageNumber: index + 1,
          overflowElementTag: overflowStartElement.tagName,
          overflowElementText: overflowStartElement.textContent.trim().replace(/\s+/g, ' ').substring(0, 100),
          relativeBottom: Math.round(overflowBottom),
          nearestHeadingBeforeOverflow: headingCandidate,
          tableCutInfo: tableCutInfo
        });
      }
    });
    
    return results;
  });

  console.log(JSON.stringify(heuristics, null, 2));
  await browser.close();
})();
