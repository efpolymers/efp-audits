document.addEventListener('DOMContentLoaded', () => {
  const fileInput = document.getElementById('file-input');
  const btnExport = document.getElementById('btn-export');
  const btnCopy = document.getElementById('btn-copy');
  const workspace = document.getElementById('workspace');
  const toolbar = document.getElementById('element-toolbar');
  const toolbarText = document.getElementById('toolbar-action-text');
  
  let allBlocks = []; 
  let currentTarget = null;
  let currentTable = null;
  let currentTableRow = null;

  let originalHeadHTML = '';

  fileInput.addEventListener('change', (e) => {
    const file = e.target.files[0];
    if (!file) return;

    const reader = new FileReader();
    reader.onload = (event) => {
      const htmlText = event.target.result;
      parseAndLoadHTML(htmlText);
      btnExport.disabled = false;
      btnCopy.disabled = false;
    };
    reader.readAsText(file);
  });

  function parseAndLoadHTML(html) {
    const parser = new DOMParser();
    const doc = parser.parseFromString(html, 'text/html');
    originalHeadHTML = doc.head.innerHTML;
    
    // Inject styles from uploaded document so it looks correct
    document.querySelectorAll('.injected-style').forEach(el => el.remove());
    doc.head.querySelectorAll('style, link[rel="stylesheet"]').forEach(el => {
       const clone = el.cloneNode(true);
       clone.classList.add('injected-style');
       document.head.appendChild(clone);
    });

    allBlocks = [];
    
    // Extract content. If already paginated, pull from .page. Otherwise, from body.
    const pages = doc.querySelectorAll('.page');
    if (pages.length > 0) {
      pages.forEach(page => {
        Array.from(page.children).forEach(child => {
          const isLetterheadImg = child.tagName === 'IMG' && child.getAttribute('src') === 'letterhead.png';
          if (!child.classList.contains('letterhead') && !child.classList.contains('doc-footer') && !isLetterheadImg) {
            allBlocks.push(child);
          }
        });
      });
    } else {
      Array.from(doc.body.children).forEach(child => {
        if (child.tagName !== 'SCRIPT' && child.id !== 'element-toolbar' && child.className !== 'studio-toolbar') {
            allBlocks.push(child);
        }
      });
    }
    
    // Set default page breaks for sections (eyebrows) if they don't have them
    allBlocks.forEach(block => {
      if (block.classList && block.classList.contains('eyebrow')) {
        if (!block.hasAttribute('data-manual-page-break')) {
          block.setAttribute('data-manual-page-break', 'true');
        }
      }
    });

    renderPages();
  }

  function renderPages() {
    workspace.innerHTML = '';
    let currentPage = createNewPage();
    
    for (let i = 0; i < allBlocks.length; i++) {
      const block = allBlocks[i];
      
      // Force new page if marked
      if (block.hasAttribute('data-manual-page-break')) {
         // Prevent empty pages: only break if current page has content besides letterhead
         if (currentPage.children.length > 1) { 
             currentPage = createNewPage();
         }
      }
      
      currentPage.appendChild(block);
      setupBlockInteraction(block);
    }
    
    updateFooters();
  }
  
  function createNewPage() {
    const page = document.createElement('div');
    page.className = 'page';
    
    const letterhead = document.createElement('img');
    letterhead.src = 'letterhead.png';
    letterhead.alt = 'Letterhead';
    letterhead.className = 'letterhead';
    letterhead.style.cssText = 'width: calc(100% + 40mm); max-width: none; height: auto; margin-left: -20mm; margin-top: -26mm; margin-bottom: 22px; display: block;';
    page.appendChild(letterhead);
    
    workspace.appendChild(page);
    return page;
  }
  
  function updateFooters() {
    const pages = workspace.querySelectorAll('.page');
    // Try to find the document title from the first H1 or H2
    let reportTitle = 'Audit Report';
    for (const block of allBlocks) {
        if (block.tagName === 'H1' || block.tagName === 'H2') {
            reportTitle = block.textContent.trim();
            break;
        }
    }

    pages.forEach((page, index) => {
      const oldFooter = page.querySelector('.doc-footer');
      if (oldFooter) oldFooter.remove();
      
      const footer = document.createElement('div');
      footer.className = 'doc-footer';
      footer.innerHTML = `<span>${reportTitle} · EF Polymer</span><span>Page ${index + 1}</span>`;
      page.appendChild(footer);
    });
  }

  // Interactive logic
  function setupBlockInteraction(block) {
    block.addEventListener('mousemove', (e) => {
      e.stopPropagation(); // Prevent bubbling to workspace
      
      if (block.tagName === 'TABLE' || block.tagName === 'TBODY') return; 
      
      currentTarget = block;
      currentTable = null;
      currentTableRow = null;
      
      const rect = block.getBoundingClientRect();
      toolbar.style.display = 'block';
      // Center toolbar above the element
      toolbar.style.top = (rect.top + window.scrollY - 30) + 'px';
      toolbar.style.left = (rect.left + window.scrollX + (rect.width/2) - 60) + 'px';
      toolbar.className = 'element-toolbar';
      
      if (block.hasAttribute('data-manual-page-break')) {
        const index = allBlocks.indexOf(block);
        if (block.tagName === 'TABLE' && index > 0 && allBlocks[index - 1].tagName === 'TABLE') {
          toolbarText.textContent = 'Merge with Previous Table';
        } else {
          toolbarText.textContent = 'Pull to Previous Page';
        }
        toolbar.style.background = '#e81123';
      } else {
        toolbarText.textContent = 'Push to Next Page';
        toolbar.style.background = '#0078d4';
      }
    });
    
    if (block.tagName === 'TABLE') {
      const rows = block.querySelectorAll('tbody tr');
      rows.forEach(row => {
        row.addEventListener('mousemove', (e) => {
          e.stopPropagation();
          currentTarget = null;
          currentTable = block;
          currentTableRow = row;
          
          const rect = row.getBoundingClientRect();
          toolbar.style.display = 'block';
          toolbar.style.top = (rect.top + window.scrollY - 30) + 'px';
          toolbar.style.left = (rect.left + window.scrollX + (rect.width/2) - 60) + 'px';
          toolbar.className = 'element-toolbar table-mode';
          toolbarText.textContent = 'Split Table Here';
        });
      });
    }
  }

  workspace.addEventListener('mousemove', (e) => {
    if (e.target === workspace || e.target.classList.contains('page')) {
      toolbar.style.display = 'none';
      currentTarget = null;
      currentTable = null;
      currentTableRow = null;
    }
  });
  
  // Keep toolbar visible when hovering over it
  toolbar.addEventListener('mousemove', (e) => {
      e.stopPropagation();
  });

  toolbar.addEventListener('click', (e) => {
    e.stopPropagation();
    if (currentTarget) {
      if (currentTarget.hasAttribute('data-manual-page-break')) {
        currentTarget.removeAttribute('data-manual-page-break');
        
        // Merge table logic
        if (currentTarget.tagName === 'TABLE') {
            const index = allBlocks.indexOf(currentTarget);
            if (index > 0 && allBlocks[index - 1].tagName === 'TABLE') {
                const prevTable = allBlocks[index - 1];
                const prevTbody = prevTable.querySelector('tbody');
                const currTbody = currentTarget.querySelector('tbody');
                
                // Move rows back
                Array.from(currTbody.children).forEach(row => prevTbody.appendChild(row));
                
                // Remove the merged table from our blocks array
                allBlocks.splice(index, 1);
            }
        }
      } else {
        currentTarget.setAttribute('data-manual-page-break', 'true');
      }
      toolbar.style.display = 'none';
      renderPages();
    } else if (currentTable && currentTableRow) {
      splitTable(currentTable, currentTableRow);
      toolbar.style.display = 'none';
    }
  });
  
  function splitTable(table, splitRow) {
    const tbody = table.querySelector('tbody');
    const rows = Array.from(tbody.children);
    const splitIndex = rows.indexOf(splitRow);
    
    // Don't split if it's the header row or if it somehow failed
    if (splitIndex <= 0) return; 
    
    // Create new table
    const newTable = document.createElement('table');
    const newTbody = document.createElement('tbody');
    newTable.appendChild(newTbody);
    
    // Move rows to new table (NO header copying as requested)
    const rowsToMove = rows.slice(splitIndex);
    rowsToMove.forEach(row => newTbody.appendChild(row));
    
    // Mark to start on new page
    newTable.setAttribute('data-manual-page-break', 'true');
    
    // Insert into global list
    const blockIndex = allBlocks.indexOf(table);
    if (blockIndex > -1) {
       allBlocks.splice(blockIndex + 1, 0, newTable);
    }
    
    renderPages();
  }

  function getFinalHTML() {
    const clone = workspace.cloneNode(true);
    return `<!DOCTYPE html>
<html lang="en">
<head>
${originalHeadHTML}
</head>
<body>
${clone.innerHTML}
</body>
</html>`;
  }

  btnExport.addEventListener('click', () => {
    const finalHtml = getFinalHTML();
    const blob = new Blob([finalHtml], { type: 'text/html' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'paginated-report.html';
    a.click();
    URL.revokeObjectURL(url);
  });

  btnCopy.addEventListener('click', () => {
    const finalHtml = getFinalHTML();
    navigator.clipboard.writeText(finalHtml).then(() => {
      const originalText = btnCopy.textContent;
      btnCopy.textContent = 'Copied!';
      setTimeout(() => {
        btnCopy.textContent = originalText;
      }, 2000);
    });
  });
});
