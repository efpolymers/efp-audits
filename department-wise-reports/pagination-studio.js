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
          if (!child.classList.contains('letterhead') && 
              !child.classList.contains('doc-footer') && 
              !child.classList.contains('delete-page-btn') && 
              !isLetterheadImg) {
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
    const wrapper = document.createElement('div');
    wrapper.className = 'page-wrapper';
    
    const headerBar = document.createElement('div');
    headerBar.className = 'page-header-bar';
    
    const pageNumSpan = document.createElement('span');
    pageNumSpan.className = 'page-number-label';
    pageNumSpan.textContent = 'Page';
    headerBar.appendChild(pageNumSpan);
    
    // Create Delete Button inside the header control bar
    const deleteBtn = document.createElement('button');
    deleteBtn.className = 'delete-page-btn';
    deleteBtn.innerHTML = '🗑️ Delete Page';
    deleteBtn.title = 'Delete this page and all its contents';
    deleteBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      const confirmDelete = confirm('Are you sure you want to delete this page and all its contents? This action cannot be undone.');
      if (!confirmDelete) return;
      
      // Find all content blocks inside the page element
      const pageChildren = Array.from(page.children);
      const blocksToDelete = pageChildren.filter(child => {
        const isLetterheadImg = child.tagName === 'IMG' && child.getAttribute('src') === 'letterhead.png';
        return !isLetterheadImg && 
               !child.classList.contains('letterhead') && 
               !child.classList.contains('doc-footer');
      });
      
      // Remove these blocks from allBlocks
      blocksToDelete.forEach(block => {
        const index = allBlocks.indexOf(block);
        if (index > -1) {
          allBlocks.splice(index, 1);
        }
      });
      
      // Re-render
      renderPages();
    });
    headerBar.appendChild(deleteBtn);
    wrapper.appendChild(headerBar);
    
    const page = document.createElement('div');
    page.className = 'page';
    
    const letterhead = document.createElement('img');
    letterhead.src = 'letterhead.png';
    letterhead.alt = 'Letterhead';
    letterhead.className = 'letterhead';
    letterhead.style.cssText = 'width: calc(100% + 40mm); max-width: none; height: auto; margin-left: -20mm; margin-top: -26mm; margin-bottom: 22px; display: block;';
    page.appendChild(letterhead);
    wrapper.appendChild(page);
    
    workspace.appendChild(wrapper);
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
      // Update page control bar label
      const wrapper = page.closest('.page-wrapper');
      if (wrapper) {
        const pageLabel = wrapper.querySelector('.page-number-label');
        if (pageLabel) {
          pageLabel.textContent = `Page ${index + 1}`;
        }
      }

      const oldFooter = page.querySelector('.doc-footer');
      if (oldFooter) oldFooter.remove();
      
      const footer = document.createElement('div');
      footer.className = 'doc-footer';
      footer.innerHTML = `<span>${reportTitle} · EF Polymer</span><span>Page ${index + 1}</span>`;
      page.appendChild(footer);
    });
  }

  // Interactive logic variables
  let currentDrillPath = [];
  let activeHoverElement = null;

  function setupBlockInteraction(block) {
    // Legacy function - we now use workspace mousemove
  }

  workspace.addEventListener('click', (e) => {
    // If clicking on the toolbar itself, don't hide it
    if (e.target.closest('#element-toolbar')) return;

    // If clicking on the sidebar controls or outside a page, clear selection
    if (e.target.closest('.page-header-bar') || !e.target.closest('.page')) {
        if (activeHoverElement) activeHoverElement.classList.remove('studio-hover');
        activeHoverElement = null;
        toolbar.style.display = 'none';
        return;
    }

    let allowedElements = [];
    if (currentDrillPath.length === 0) {
        allowedElements = allBlocks;
    } else {
        const parent = currentDrillPath[currentDrillPath.length - 1];
        allowedElements = Array.from(parent.children);
    }

    // Find the deepest allowed element that was clicked
    let targetEl = null;
    for (let el of allowedElements) {
        if (el === e.target || el.contains(e.target)) {
            targetEl = el;
            break;
        }
    }

    if (targetEl) {
        if (activeHoverElement && activeHoverElement !== targetEl) {
            activeHoverElement.classList.remove('studio-hover');
        }
        activeHoverElement = targetEl;
        activeHoverElement.classList.add('studio-hover');
        showToolbar(targetEl);
    } else {
        // Clicked inside the page but not on a block (e.g. padding)
        if (activeHoverElement) activeHoverElement.classList.remove('studio-hover');
        activeHoverElement = null;
        toolbar.style.display = 'none';
    }
  });

  function showToolbar(el) {
    const rect = el.getBoundingClientRect();
    toolbar.style.display = 'flex';
    toolbar.style.top = (rect.top + window.scrollY - 30) + 'px';
    toolbar.style.left = (rect.left + window.scrollX + (rect.width/2) - (toolbar.offsetWidth/2)) + 'px';
    
    const btnUp = document.getElementById('toolbar-btn-up');
    const btnDown = document.getElementById('toolbar-btn-down');
    
    if (currentDrillPath.length > 0) {
        btnUp.style.display = 'inline-block';
    } else {
        btnUp.style.display = 'none';
    }
    
    let hasElementChildren = false;
    for (let i = 0; i < el.children.length; i++) {
        if (el.children[i].tagName !== 'BR') {
            hasElementChildren = true;
            break;
        }
    }
    
    if (hasElementChildren && el.tagName !== 'SVG') {
        btnDown.style.display = 'inline-block';
    } else {
        btnDown.style.display = 'none';
    }

    if (el.hasAttribute('data-manual-page-break')) {
        toolbarText.textContent = 'Pull to Previous Page';
        toolbar.style.background = '#e81123';
    } else {
        toolbarText.textContent = 'Push to Next Page';
        toolbar.style.background = '#0078d4';
    }
  }

  document.getElementById('toolbar-btn-up').addEventListener('click', (e) => {
      e.stopPropagation();
      if (currentDrillPath.length > 0) {
          currentDrillPath.pop();
          if (activeHoverElement) activeHoverElement.classList.remove('studio-hover');
          activeHoverElement = null;
          toolbar.style.display = 'none';
      }
  });

  document.getElementById('toolbar-btn-down').addEventListener('click', (e) => {
      e.stopPropagation();
      if (activeHoverElement) {
          currentDrillPath.push(activeHoverElement);
          activeHoverElement.classList.remove('studio-hover');
          activeHoverElement = null;
          toolbar.style.display = 'none';
      }
  });

  document.getElementById('toolbar-action-text').addEventListener('click', (e) => {
      e.stopPropagation();
      if (!activeHoverElement) return;

      if (currentDrillPath.length === 0) {
          if (activeHoverElement.hasAttribute('data-manual-page-break')) {
              activeHoverElement.removeAttribute('data-manual-page-break');
              const index = allBlocks.indexOf(activeHoverElement);
              if (activeHoverElement.tagName === 'TABLE' && index > 0 && allBlocks[index - 1].tagName === 'TABLE') {
                  const prevTable = allBlocks[index - 1];
                  const prevTbody = prevTable.querySelector('tbody');
                  const currTbody = activeHoverElement.querySelector('tbody');
                  if (prevTbody && currTbody) {
                      Array.from(currTbody.children).forEach(row => prevTbody.appendChild(row));
                      allBlocks.splice(index, 1);
                  }
              }
          } else {
              activeHoverElement.setAttribute('data-manual-page-break', 'true');
          }
      } else {
          const topLevelBlock = currentDrillPath[0];
          performDeepSplit(topLevelBlock, activeHoverElement);
          currentDrillPath = []; // reset drill path
      }
      
      if (activeHoverElement) activeHoverElement.classList.remove('studio-hover');
      activeHoverElement = null;
      toolbar.style.display = 'none';
      renderPages();
  });

  function performDeepSplit(topLevelBlock, targetEl) {
      let path = [];
      let curr = targetEl;
      while (curr && curr !== topLevelBlock) {
          path.push(curr);
          curr = curr.parentElement;
      }
      if (curr !== topLevelBlock) return;
      path.push(topLevelBlock);
      path.reverse(); 

      let newTopLevelBlock = topLevelBlock.cloneNode(false);
      newTopLevelBlock.setAttribute('data-manual-page-break', 'true');
      
      let currentNewNode = newTopLevelBlock;

      for (let i = 1; i < path.length; i++) {
          let targetChild = path[i];
          
          if (i === path.length - 1) {
              let sibling = targetChild;
              while (sibling) {
                  let nextSibling = sibling.nextSibling;
                  currentNewNode.appendChild(sibling);
                  sibling = nextSibling;
              }
          } else {
              let newChild = targetChild.cloneNode(false);
              currentNewNode.appendChild(newChild);
              
              let sibling = targetChild.nextSibling;
              while (sibling) {
                  let nextSibling = sibling.nextSibling;
                  currentNewNode.appendChild(sibling);
                  sibling = nextSibling;
              }
              currentNewNode = newChild;
          }
      }
      
      const blockIndex = allBlocks.indexOf(topLevelBlock);
      if (blockIndex > -1) {
         allBlocks.splice(blockIndex + 1, 0, newTopLevelBlock);
      }
  }

  function getFinalHTML() {
    const pages = workspace.querySelectorAll('.page');
    let pagesHTML = '';
    pages.forEach(page => {
      const pageClone = page.cloneNode(true);
      pageClone.querySelectorAll('.delete-page-btn').forEach(btn => btn.remove());
      pageClone.classList.remove('active');
      pagesHTML += pageClone.outerHTML + '\n';
    });
    return `<!DOCTYPE html>
<html lang="en">
<head>
${originalHeadHTML}
</head>
<body>
${pagesHTML}
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
