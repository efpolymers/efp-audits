import os
import glob
import re

directory = '/Users/manishbulchandani/D/Creative Upaay/Work/ef-polymers/Audit-using-skils/department-wise-reports'
files = glob.glob(os.path.join(directory, '*.html'))
files.sort()

with open('all_solutions_text.md', 'w', encoding='utf-8') as out_f:
    for filepath in files:
        filename = os.path.basename(filepath)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract everything between <h2>Recommended Solution Segment</h2> and <div class="doc-footer"> or <h3>Future Scope
        match = re.search(r'<h2>Recommended Solution Segment</h2>(.*?)<h3>Future Scope', content, re.IGNORECASE | re.DOTALL)
        if not match:
            match = re.search(r'<h2>Recommended Solution Segment</h2>(.*?)(?:<h3>Next Steps|<div class="doc-footer">)', content, re.IGNORECASE | re.DOTALL)
            
        out_f.write(f"## {filename}\n")
        if match:
            # strip html tags
            text = re.sub(r'<[^>]+>', ' ', match.group(1))
            # replace multiple spaces with single space
            text = re.sub(r'\s+', ' ', text)
            out_f.write(text.strip() + "\n\n")
        else:
            out_f.write("No Recommended Solution Segment found.\n\n")

