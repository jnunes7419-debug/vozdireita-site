import os
import glob
import re

html_files = glob.glob('d:/direita_intelectual/*.html')
favicon_tag = '\n    <link rel="icon" type="image/png" href="assets/favicon.png">'

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if favicon already exists
    if 'rel="icon"' in content or 'rel="shortcut icon"' in content:
        continue
    
    # Inject just after <head>
    new_content = re.sub(r'(<head.*?>)', r'\1' + favicon_tag, content, count=1, flags=re.IGNORECASE)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
            
print(f"Favicon adicionado a {len(html_files)} arquivos HTML.")
