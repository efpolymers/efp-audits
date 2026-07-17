import os
import re

tool_map = {
    'whatsapp': 'https://img.icons8.com/color/48/000000/whatsapp--v1.png',
    'slack': 'https://img.icons8.com/color/48/000000/slack-new.png',
    'wechat': 'https://cdn.simpleicons.org/wechat/07C160',
    'line': 'https://img.icons8.com/color/48/000000/line-me.png',
    'zoho': 'https://cdn.worldvectorlogo.com/logos/zoho-1.svg',
    'google sheet': 'https://img.icons8.com/color/48/000000/google-sheets.png',
    'google drive': 'https://img.icons8.com/color/48/000000/google-drive--v2.png',
    'google doc': 'https://img.icons8.com/color/48/000000/google-docs--v2.png',
    'google slide': 'https://img.icons8.com/color/48/000000/google-slides.png',
    'google calendar': 'https://img.icons8.com/color/48/000000/google-calendar--v2.png',
    'google ads': 'https://img.icons8.com/color/48/000000/google-ads.png',
    'gmail': 'https://img.icons8.com/color/48/000000/gmail-new.png',
    'canva': 'https://img.icons8.com/color/48/000000/canva.png',
    'powerpoint': 'https://img.icons8.com/color/48/000000/microsoft-powerpoint-2019.png',
    'excel': 'https://img.icons8.com/color/48/000000/microsoft-excel-2019.png',
    'linkedin': 'https://img.icons8.com/color/48/000000/linkedin.png',
    'power bi': 'https://img.icons8.com/color/48/000000/power-bi-2021.png',
    'chatgpt': 'https://img.icons8.com/color/48/000000/chatgpt.png',
    'indeed': 'https://cdn.simpleicons.org/indeed/003A9B',
    'facebook': 'https://img.icons8.com/color/48/000000/facebook-new.png',
    'instagram': 'https://img.icons8.com/color/48/000000/instagram-new.png',
    'naukri': 'https://img.icons8.com/color/48/000000/briefcase.png',
    'apollo': 'https://img.icons8.com/color/48/000000/apollo.png',
    'salesiq': 'https://cdn.worldvectorlogo.com/logos/zoho-1.svg',
    'contactout': 'https://img.icons8.com/color/48/000000/search--v1.png',
    'dripify': 'https://img.icons8.com/color/48/000000/bot.png'
}

dir_path = "/Users/manishbulchandani/D/Creative Upaay/Work/ef-polymers/Audit-using-skils/department-wise-reports"

def process_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    def replacer(match):
        pre_icon = match.group(1)
        old_icon = match.group(2)
        mid = match.group(3)
        tool_name = match.group(4)
        post_name = match.group(5)
        
        lower_name = tool_name.lower()
        found_icons = []
        
        for key, url in tool_map.items():
            if key in lower_name:
                found_icons.append(url)
        
        if 'email' in lower_name and 'gmail' not in lower_name:
            found_icons.append(tool_map['gmail'])
            
        if not found_icons:
            if 'social platforms' in lower_name:
                found_icons = [tool_map['linkedin'], tool_map['facebook'], tool_map['instagram']]
            else:
                return match.group(0)
        
        if len(found_icons) == 1:
            new_icon = f'<img src="{found_icons[0]}" width="24" height="24" style="display:block; object-fit:contain;" alt="{tool_name}" />'
        else:
            imgs = [f'<img src="{i}" width="24" height="24" style="display:block; object-fit:contain;" alt="{tool_name}" />' for i in found_icons]
            new_icon = f'<div style="display:flex; gap:6px;">{"".join(imgs)}</div>'
            
        return pre_icon + new_icon + mid + tool_name + post_name

    new_content = re.sub(
        r'(<div class="tool-icon"[^>]*>)(.*?)(</div>\s*<div[^>]*>\s*<div class="tool-name">)(.*?)(</div>)',
        replacer,
        content,
        flags=re.DOTALL
    )
    
    if new_content != content:
        with open(filepath, 'w') as f:
            f.write(new_content)
        print(f"Updated {filepath}")

for file in os.listdir(dir_path):
    if file.endswith(".html"):
        process_file(os.path.join(dir_path, file))
