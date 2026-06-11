import os
import glob

def increase_font(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # For index.html: increase the size of paragraph texts in cards
    if "index.html" in filepath:
        # Pôsteres/Cards text: class="text-zinc-600 dark:text-zinc-400 text-xs font-light leading-relaxed flex-grow"
        # Let's just find `text-xs font-light` and `text-sm font-light` inside <p> or general tags
        content = content.replace('text-xs font-light leading-relaxed', 'text-sm font-light leading-relaxed')
        content = content.replace('text-sm font-light text-zinc-600', 'text-base font-light text-zinc-600') # Sections subtitle
        
    # For Dossiers (e.g. analise-oglobo-rosa.html):
    # The main article text is inside <div class="... text-sm md:text-base ...">
    content = content.replace('text-sm md:text-base leading-relaxed', 'text-base md:text-lg leading-relaxed')
    
    # Blockquotes text size
    content = content.replace('text-sm md:text-base italic', 'text-base md:text-lg italic')
    
    # Bullet points text size
    content = content.replace('text-sm text-zinc-700', 'text-base text-zinc-700')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

for html_file in glob.glob("d:/direita_intelectual/*.html"):
    increase_font(html_file)

print("Font sizes increased across all HTML files.")
