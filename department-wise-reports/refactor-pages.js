const fs = require('fs');
const path = require('path');

const htmlPath = path.join(__dirname, '00-overall-analysis.html');
let html = fs.readFileSync(htmlPath, 'utf8');

// The heuristics we found:
const splits = [
  {
    pageId: 2,
    type: 'heading',
    text: '<h3>Critical Observations</h3>'
  },
  {
    pageId: 3,
    type: 'table-row',
    text: '<tr><td><strong>Packaging Languages</strong></td><td>Hindi, English, Spanish, French, Japanese + custom</td></tr>'
  },
  {
    pageId: 4,
    type: 'heading',
    text: '<h3>Headcount Distribution</h3>'
  },
  {
    pageId: 5,
    type: 'heading',
    text: '<h3>Department Maturity Scorecard</h3>'
  },
  {
    pageId: 6,
    type: 'table-row', // "MENA & Intl Sales..."
    text: '<tr><td><strong>MENA &amp; Intl Sales</strong></td>'
  },
  {
    pageId: 7,
    type: 'table-row', // Critical Dependency Matrix, cut after Accounts -> Production
    text: '<tr><td><strong>Production → Sales/BD</strong></td>'
  },
  {
    pageId: 8,
    type: 'table-row', // Critical Risk Register, cut after R08
    text: '<tr><td class="id">R09</td>'
  },
  {
    pageId: 9,
    type: 'heading',
    text: '<h3>Operational Truth Gaps</h3>'
  },
  {
    pageId: 10,
    type: 'table-row', // Digital Maturity Index, cut after Process Digitization
    text: '<tr><td><strong>Reporting Capability</strong></td>'
  },
  {
    pageId: 11,
    type: 'heading',
    text: '<h3>Data Quality Score</h3>'
  },
  {
    pageId: 12,
    type: 'heading',
    text: '<h3>Identified Bottlenecks</h3>'
  },
  {
    pageId: 13,
    type: 'table-row', // AI Opportunity Register, cut after AI-03
    text: '<tr><td class="id">AI-04</td>'
  },
  {
    pageId: 14,
    type: 'heading',
    text: '<h3>The Seven Shared Platforms</h3>'
  },
  {
    pageId: 15,
    type: 'table-row', // Platform to dept, cut after Finance
    text: '<tr><td><strong>Marketing / Retail</strong></td>'
  },
  {
    pageId: 16,
    type: 'table-row', // Capacity breakdown, cut after COO Office
    text: '<tr><td><strong>Marketing / Retail</strong></td><td>~1,680</td>'
  }
];

// Let's do replacements
// A split means replacing the target text with:
// <div class="doc-footer"><span>Overall Analysis · EF Polymer · v2.0</span><span>Page X</span></div>
// </div>
// <div class="page">
// <img src="letterhead.png" alt="Letterhead" class="letterhead" />
// <target text>
// (for tables we also need to close and reopen the table)

for (const split of splits) {
  if (split.type === 'heading') {
    const replacement = `    <div class="doc-footer"><span>Overall Analysis · EF Polymer · v2.0</span><span>Page X</span></div>
  </div>

  <div class="page">
    <img src="letterhead.png" alt="Letterhead" class="letterhead" />
    ${split.text}`;
    html = html.replace(split.text, replacement);
  } else if (split.type === 'table-row') {
    // Need to close the table, end the page, start new page, start table and add headers if possible.
    // To keep it simple, we just find the table header by looking back, but maybe we can just reopen the table.
    // Actually, without headers it looks a bit bare, but let's just close/reopen table.
    const replacement = `</table>
    <div class="doc-footer"><span>Overall Analysis · EF Polymer · v2.0</span><span>Page X</span></div>
  </div>

  <div class="page">
    <img src="letterhead.png" alt="Letterhead" class="letterhead" />
    <table>
      ${split.text}`;
    html = html.replace(split.text, replacement);
  }
}

// Now we need to recalculate all page numbers
let pageCounter = 1;
html = html.replace(/<div class="doc-footer"><span>(.*?)<\/span><span>Page X?.*?<\/span><\/div>/g, () => {
  const replacement = `<div class="doc-footer"><span>Overall Analysis · EF Polymer · v2.0</span><span>Page ${pageCounter}</span></div>`;
  pageCounter++;
  return replacement;
});

// Since the original document had page numbers like Page 1, Page 2... we should replace all of them.
// Let's just do a generic regex for doc footer
let counter = 1;
html = html.replace(/<div class="doc-footer"><span>(.*?)<\/span><span>.*?<\/span><\/div>/g, (match, p1) => {
  return `<div class="doc-footer"><span>${p1}</span><span>Page ${counter++}</span></div>`;
});

fs.writeFileSync(path.join(__dirname, '00-overall-analysis-refactored.html'), html);
console.log('Refactored HTML written to 00-overall-analysis-refactored.html');
