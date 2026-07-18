const puppeteer = require('puppeteer');
const fs = require('fs');
const path = require('path');

const CHROME_PATH = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
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

async function generatePdf(inputPath, outPdfPath) {
  const browser = await puppeteer.launch(launchOpts());
  const page = await browser.newPage();
  
  await withAuthBypass(page);
  
  console.log(`Loading HTML from: ${inputPath}`);
  await page.goto(`file://${inputPath}`, { waitUntil: 'networkidle0' });
  
  // Inject print styles to force exact A4 bounds and hide footers
  await page.addStyleTag({
    content: `
      @page { margin: 0px !important; size: A4; }
      body { background: transparent !important; margin: 0 !important; padding: 0 !important; }
      .page { 
        margin: 0 !important; 
        box-shadow: none !important; 
        width: 210mm !important;
        height: 297mm !important;
        min-height: 297mm !important;
        max-height: 297mm !important;
        box-sizing: border-box !important;
        overflow: hidden !important;
        padding: 26mm 20mm 20mm 20mm !important;
      }
      .doc-footer { display: none !important; }
    `
  });

  console.log(`Generating PDF...`);
  await page.pdf({
    path: outPdfPath,
    format: 'A4',
    printBackground: true,
    margin: { top: '0px', right: '0px', bottom: '0px', left: '0px' }
  });
  
  await browser.close();
  console.log(`✅ PDF generated: ${outPdfPath}`);
}

async function main() {
  const targetFile = process.argv[2] || '00.html';
  const inputPath = path.resolve(__dirname, targetFile);
  
  if (!fs.existsSync(inputPath)) {
    console.error(`❌ File not found: ${inputPath}`);
    process.exit(1);
  }

  const parsedPath = path.parse(inputPath);
  const outPdfPath = path.join(parsedPath.dir, `${parsedPath.name}.pdf`);

  console.log(`🚀 Starting PDF generation for ${targetFile}...`);
  await generatePdf(inputPath, outPdfPath);
}

main();
