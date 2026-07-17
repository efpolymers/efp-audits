import os
import glob
import re
import json

directory = '/Users/manishbulchandani/D/Creative Upaay/Work/ef-polymers/Audit-using-skils/department-wise-reports'
files = glob.glob(os.path.join(directory, '*.html'))
files.sort()

results = {}

for filepath in files:
    filename = os.path.basename(filepath)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Let's count how many times "sol-card" appears
    # Or just try to find all solutions.
    solutions = []
    
    # Try to find all sol-card divs and their titles.
    # regex to find title: <div class="sol-title">TITLE</div>
    
    # If there are no sol-cards, maybe they use <h3>
    titles = re.findall(r'<div class="sol-title">(.*?)</div>', content, re.IGNORECASE | re.DOTALL)
    
    if titles:
        for t in titles:
            solutions.append({"title": t.strip()})
    else:
        # Some might use <h3> for solutions under the solutions section
        # Let's just find anything under the Solutions h2.
        # This is harder to do precisely with regex.
        # Let's count the number of <h3> under the Proposed Solutions section.
        # Just find the section first.
        match = re.search(r'<h2[^>]*>.*?(?:Proposed Tech Solutions|Solutions).*?</h2>(.*?)<h2', content, re.IGNORECASE | re.DOTALL)
        if not match:
            # Maybe it's the last section
            match = re.search(r'<h2[^>]*>.*?(?:Proposed Tech Solutions|Solutions).*?</h2>(.*)', content, re.IGNORECASE | re.DOTALL)
            
        if match:
            section_content = match.group(1)
            h3s = re.findall(r'<h3[^>]*>(.*?)</h3>', section_content, re.IGNORECASE | re.DOTALL)
            for h3 in h3s:
                solutions.append({"title": h3.strip()})

    results[filename] = solutions

with open('extracted_solutions.json', 'w') as f:
    json.dump(results, f, indent=2)

print("Extraction complete. Found solutions in", len(results), "files.")
