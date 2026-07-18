const puppeteer = require('puppeteer');
const fs = require('fs');
const path = require('path');

const reportsDir = __dirname;
const outputDir = path.join(reportsDir, 'pdf_reports');

// Create output directory if it doesn't exist
if (!fs.existsSync(outputDir)) {
  fs.mkdirSync(outputDir, { recursive: true });
}

async function convertFileToPdf(browser, fileName) {
  const filePath = path.join(reportsDir, fileName);
  if (!fs.existsSync(filePath)) {
    console.error(`❌ Error: File not found: ${fileName}`);
    return;
  }

  const outputFileName = fileName.replace('.html', '.pdf');
  const outputPath = path.join(outputDir, outputFileName);
  
  const page = await browser.newPage();
  
  // Inject localStorage token to bypass auth.js passcode check
  await page.evaluateOnNewDocument(() => {
    localStorage.setItem('reports_auth_expiry', (Date.now() + 2 * 60 * 60 * 1000).toString());
  });
  
  try {
    // Load local file URL
    const fileUrl = `file://${filePath}`;
    console.log(`⏳ Converting ${fileName}...`);
    
    // Wait for networkidle0 to ensure all images and fonts are loaded
    await page.goto(fileUrl, { waitUntil: 'networkidle0' });
    
    // Inject style to override HTML @page margins, body background and page container margins
    await page.addStyleTag({
      content: `
        @page {
          margin: 0px !important;
        }
        body {
          background: transparent !important;
          zoom: ${process.env.PDF_ZOOM || '0.94'} !important;
        }
        .page {
          margin: 0px auto 0px auto !important;
          box-shadow: none !important;
        }
      `
    });
    
    // Convert to PDF
    await page.pdf({
      path: outputPath,
      format: 'A4',
      printBackground: true, // Print CSS backgrounds
      margin: {
        top: '0px',
        right: '0px',
        bottom: '0px',
        left: '0px'
      }
    });
    
    console.log(`✅ Successfully generated: ${outputFileName}`);
  } catch (error) {
    console.error(`❌ Failed to convert ${fileName}:`, error.message);
  } finally {
    await page.close();
  }
}

async function main() {
  // Get filename argument if provided
  const targetFile = process.argv[2];
  
  console.log('🚀 Starting PDF generation...');
  
  const chromePath = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
  const launchOptions = {
    headless: 'new'
  };
  
  if (fs.existsSync(chromePath)) {
    console.log(`ℹ️ Using system Chrome at: ${chromePath}`);
    launchOptions.executablePath = chromePath;
  }

  const browser = await puppeteer.launch(launchOptions);

  try {
    if (targetFile) {
      // Convert a single file
      if (!targetFile.endsWith('.html')) {
        console.error('❌ Please provide an HTML file (e.g. report.html)');
        process.exit(1);
      }
      await convertFileToPdf(browser, targetFile);
    } else {
      // Convert all HTML files in the directory
      console.log('📂 No specific file provided. Converting all HTML files in the directory...');
      
      const files = fs.readdirSync(reportsDir);
      const htmlFiles = files.filter(file => file.endsWith('.html') && file !== 'index.html');
      
      if (htmlFiles.length === 0) {
        console.log('⚠️ No HTML files found in the directory.');
        return;
      }
      
      console.log(`Found ${htmlFiles.length} HTML files.`);
      
      // Process sequentially to avoid memory issues with many files
      for (const file of htmlFiles) {
        await convertFileToPdf(browser, file);
      }
      
      console.log('🎉 All files converted successfully!');
    }
  } catch (error) {
    console.error('❌ An unexpected error occurred:', error);
  } finally {
    await browser.close();
    console.log(`📁 PDF files are saved in: ${outputDir}`);
  }
}

main();
