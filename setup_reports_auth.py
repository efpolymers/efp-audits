import os
import glob
import re

WORKSPACE_DIR = "/Users/manishbulchandani/D/Creative Upaay/Work/ef-polymers/Audit-using-skils"
REPORTS_DIR = os.path.join(WORKSPACE_DIR, "department-wise-reports")
ENV_FILE = os.path.join(WORKSPACE_DIR, ".env")

# Proper names mapping
REPORT_NAMES = {
    "00-overall-analysis.html": "Overall Analysis",
    "01-ceo-report-final.html": "CEO Office",
    "02-operations-coo-office.html": "Operations & COO Office",
    "03-sales-bd-cbdo-office.html": "Sales, BD & CBDO Office",
    "04a-bd-cocopeat.html": "Business Development - Cocopeat",
    "04b-bd-seed.html": "Business Development - Seed",
    "04c-bd-ngo-csr.html": "Business Development - NGO & CSR",
    "04d-bd-government.html": "Business Development - Government",
    "04e-bd-b2b-rcm.html": "Business Development - B2B & RCM",
    "05-mena-international-sales.html": "MENA & International Sales",
    "06-finance-accounts.html": "Finance & Accounts",
    "07-marketing-retail-sales.html": "Marketing & Retail Sales",
    "08-production-qc.html": "Production & Quality Control",
    "09-research-development.html": "Research & Development",
    "10-logistics.html": "Logistics",
    "11-hr-talent-management.html": "HR & Talent Management",
    "roadmap.html": "Unified 1-Year Transformation Roadmap",
}

# 1. Handle .env and get passcode
passcode = "EFPolymer2026"
if not os.path.exists(ENV_FILE):
    with open(ENV_FILE, "w") as f:
        f.write(f"REPORT_PASSCODE={passcode}\n")
else:
    with open(ENV_FILE, "r") as f:
        for line in f:
            if line.startswith("REPORT_PASSCODE="):
                passcode = line.strip().split("=", 1)[1]
                break

# 2. Generate auth.js (Removed copy link logic from here)
auth_js_content = f"""(function() {{
    const PASSCODE = "{passcode}";
    const AUTH_KEY = 'reports_auth_expiry';
    const AUTH_DURATION = 2 * 60 * 60 * 1000; // 2 hours

    function checkAuth() {{
        const expiry = localStorage.getItem(AUTH_KEY);
        if (expiry && Date.now() < parseInt(expiry)) {{
            localStorage.setItem(AUTH_KEY, Date.now() + AUTH_DURATION);
            return true;
        }}
        return false;
    }}

    function initAuthUI() {{
        const authDiv = document.createElement('div');
        authDiv.id = 'auth-overlay';
        authDiv.style.cssText = 'position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; background: #EDEFF1; z-index: 2147483647; display: flex; flex-direction: column; align-items: center; justify-content: center; font-family: "Segoe UI", system-ui, sans-serif;';
        
        authDiv.innerHTML = `
            <div style="background: white; padding: 40px; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.05); text-align: center; max-width: 400px; width: 90%; border: 1px solid #D8DEE5;">
                <h2 style="color: #3F4B5C; margin-bottom: 8px; font-size: 20px; font-weight: 600;">Restricted Access</h2>
                <p style="color: #6B7785; margin-bottom: 24px; font-size: 14px;">Please enter the passcode to view this document.</p>
                <div style="display: flex; flex-direction: column; gap: 12px;">
                    <input type="password" id="auth-passcode" placeholder="Enter Passcode" style="padding: 10px 14px; border: 1px solid #D8DEE5; border-radius: 4px; font-size: 14px; outline: none;" onfocus="this.style.borderColor='#6b4fc8'" onblur="this.style.borderColor='#D8DEE5'">
                    <button id="auth-submit" style="padding: 10px 14px; background: #3F4B5C; color: white; border: none; border-radius: 4px; font-size: 14px; font-weight: 500; cursor: pointer;">Unlock Document</button>
                    <div id="auth-error" style="color: #A32E24; font-size: 13px; display: none; margin-top: 8px;">Incorrect passcode. Please try again.</div>
                </div>
            </div>
        `;
        
        // Hide all original content
        Array.from(document.body.children).forEach(child => {{
            if(child.id !== 'auth-overlay') child.style.display = 'none';
        }});
        
        document.body.appendChild(authDiv);
        document.documentElement.style.display = ''; 
        
        const submitBtn = authDiv.querySelector('#auth-submit');
        const inputField = authDiv.querySelector('#auth-passcode');
        
        const attemptUnlock = () => {{
            if (inputField.value === PASSCODE) {{
                localStorage.setItem(AUTH_KEY, Date.now() + AUTH_DURATION);
                window.location.reload();
            }} else {{
                authDiv.querySelector('#auth-error').style.display = 'block';
                inputField.value = '';
            }}
        }};

        submitBtn.addEventListener('click', attemptUnlock);
        inputField.addEventListener('keypress', (e) => {{
            if (e.key === 'Enter') attemptUnlock();
        }});
    }}

    if (!checkAuth()) {{
        document.documentElement.style.display = 'none'; 
        document.addEventListener('DOMContentLoaded', initAuthUI);
    }}
}})();
"""

with open(os.path.join(REPORTS_DIR, "auth.js"), "w") as f:
    f.write(auth_js_content)


# 3. Generate index.html with professional list view
reports = glob.glob(os.path.join(REPORTS_DIR, "*.html"))
reports = [os.path.basename(r) for r in reports if not os.path.basename(r) == "index.html"]
reports.sort()

# Move roadmap to the top
if "roadmap.html" in reports:
    reports.remove("roadmap.html")
    reports.insert(0, "roadmap.html")

def generate_item_html(r):
    title = REPORT_NAMES.get(r, r.replace('.html', ''))
    r_link = r.replace('.html', '')
    return f"""
        <div class="list-item">
            <div class="item-info">
                <div class="item-icon">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                        <polyline points="14 2 14 8 20 8"></polyline>
                        <line x1="16" y1="13" x2="8" y2="13"></line>
                        <line x1="16" y1="17" x2="8" y2="17"></line>
                        <polyline points="10 9 9 9 8 9"></polyline>
                    </svg>
                </div>
                <div class="item-title">{title}</div>
            </div>
            <div class="item-actions">
                <button class="btn btn-secondary" onclick="copyLink('{r_link}', this)">
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path>
                        <path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path>
                    </svg>
                    Copy Link
                </button>
                <button class="btn btn-primary" onclick="window.open('{r_link}', '_blank')">
                    Open Report
                </button>
            </div>
        </div>
"""

list_html = '<h2 style="font-size: 14px; color: var(--muted); padding: 16px 20px 4px; margin: 0; text-transform: uppercase; letter-spacing: 0.5px;">Overall</h2>'
overall_files = ["roadmap.html", "00-overall-analysis.html"]
for r in overall_files:
    if r in reports:
        list_html += generate_item_html(r)
        reports.remove(r)

list_html += '<h2 style="font-size: 14px; color: var(--muted); padding: 16px 20px 4px; margin: 0; border-top: 1px solid var(--line); text-transform: uppercase; letter-spacing: 0.5px;">Department Wise Reports</h2>'
for r in reports:
    list_html += generate_item_html(r)

index_html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EF Polymer | Department Audit Reports</title>
    <script src="auth.js"></script>
    <style>
        :root {{
            --slate: #3F4B5C;
            --muted: #6B7785;
            --bg: #F6F7F9;
            --paper: #FFFFFF;
            --line: #E9EDF1;
            --primary: #2C3545;
        }}
        body {{
            font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
            background: var(--bg);
            color: var(--slate);
            margin: 0;
            padding: 40px 20px;
            min-height: 100vh;
        }}
        .container {{
            max-width: 900px;
            margin: 0 auto;
        }}
        .header {{
            margin-bottom: 40px;
            padding-bottom: 20px;
            border-bottom: 1px solid var(--line);
        }}
        .header h1 {{
            color: var(--primary);
            font-size: 24px;
            margin: 0 0 8px 0;
            font-weight: 600;
        }}
        .header p {{
            color: var(--muted);
            font-size: 14px;
            margin: 0;
        }}
        .list-container {{
            background: var(--paper);
            border: 1px solid var(--line);
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.02);
        }}
        .list-item {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 16px 20px;
            border-bottom: 1px solid var(--line);
        }}
        .list-item:last-child {{
            border-bottom: none;
        }}
        .item-info {{
            display: flex;
            align-items: center;
            gap: 16px;
        }}
        .item-icon {{
            color: var(--muted);
            display: flex;
            align-items: center;
        }}
        .item-title {{
            font-size: 15px;
            font-weight: 500;
            color: var(--primary);
        }}
        .item-actions {{
            display: flex;
            gap: 12px;
        }}
        .btn {{
            display: flex;
            align-items: center;
            gap: 6px;
            padding: 8px 14px;
            border-radius: 4px;
            font-size: 13px;
            font-weight: 500;
            cursor: pointer;
            border: 1px solid transparent;
            font-family: inherit;
        }}
        .btn-secondary {{
            background: transparent;
            border-color: var(--line);
            color: var(--slate);
        }}
        .btn-secondary:hover {{
            background: var(--bg);
        }}
        .btn-primary {{
            background: var(--primary);
            color: white;
        }}
        .btn-primary:hover {{
            background: #1a202c;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Department Audit Reports</h1>
            <p>Internal documentation and strategic analysis</p>
        </div>
        <div class="list-container">
            {list_html}
        </div>
    </div>
    
    <script>
        function copyLink(path, btn) {{
            const url = window.location.href.replace(/[^/]*$/, '') + path;
            navigator.clipboard.writeText(url).then(() => {{
                const originalHtml = btn.innerHTML;
                btn.innerHTML = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg> Copied';
                setTimeout(() => {{
                    btn.innerHTML = originalHtml;
                }}, 2000);
            }});
        }}
    </script>
</body>
</html>
"""
with open(os.path.join(REPORTS_DIR, "index.html"), "w") as f:
    f.write(index_html_content)


# 4. Clean up and inject auth script into all report HTML files
all_reports_files = glob.glob(os.path.join(REPORTS_DIR, "*.html"))
for filepath in all_reports_files:
    r_name = os.path.basename(filepath)
    if r_name == "index.html": continue
    
    with open(filepath, "r") as f:
        content = f.read()
    
    # Remove any messed up \\n literal if it exists
    content = content.replace("<head>\\n  <script src='auth.js'></script>", "<head>")
    content = content.replace("<head>\\n  <script src=\"auth.js\"></script>", "<head>")
    
    # Fix letterhead path (no longer in parent dir)
    content = content.replace("../letterhead.png", "letterhead.png")
    
    # Force desktop-like fixed width viewport for PDF-like zooming on mobile
    content = content.replace('<meta name="viewport" content="width=device-width, initial-scale=1.0">', '<meta name="viewport" content="width=880">')
    
    # Check if already correctly injected
    if "<head>\n  <script src='auth.js'></script>" not in content and '<script src="auth.js"></script>' not in content and "<script src='auth.js'></script>" not in content:
        # Inject right after <head> using proper newline
        if "<head>" in content:
            content = content.replace("<head>", "<head>\\n  <script src='auth.js'></script>", 1)
            content = content.replace("<head>\\n  <script src='auth.js'></script>", "<head>\n  <script src='auth.js'></script>")
        else:
            print(f"Warning: No <head> tag found in {r_name}")
            
    with open(filepath, "w") as f:
        f.write(content)
        
    print(f"Processed {r_name}")

print("Setup complete.")
