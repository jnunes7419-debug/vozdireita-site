import sys
import re
import argparse

def main():
    parser = argparse.ArgumentParser(description="Add a new dossier to Voz Direita index.html")
    parser.add_argument('--url', required=True, help="URL of the new dossier (e.g. analise-nova.html)")
    parser.add_argument('--img', required=True, help="Image path (e.g. assets/imagem.png)")
    parser.add_argument('--title', required=True, help="Title of the article")
    parser.add_argument('--desc', required=True, help="Description of the article")
    parser.add_argument('--tag', required=True, help="Tag (e.g. INTERCEPTADO | CARTA CAPITAL)")
    parser.add_argument('--date', required=True, help="Date string (e.g. 09 de Junho, 2026)")
    
    args = parser.parse_args()

    file_path = 'd:\\direita_intelectual\\index.html'
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print("index.html not found.")
        return

    # 1. Update Search Array
    print("Updating search array...")
    search_entry = f"""
        {{
            title: '{args.title}',
            desc: '{args.desc}',
            img: '{args.img}',
            url: '{args.url}'
        }},"""
    
    match_search = re.search(r'articles:\s*\[(.*?)\]', content, re.DOTALL)
    if match_search and args.url not in match_search.group(1):
        content = re.sub(r'(articles:\s*\[)', r'\1\n' + search_entry, content)
    else:
        print("Article already in search array or array not found.")

    # 2. Update Main Cards
    print("Updating main cards...")
    start_pattern = r'<div id="radar-grid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">\s*'
    end_pattern = r'\s*</div>\s*</section>\s*<!-- SEÇÃO MAIS ARTIGOS \(MINIATURAS\) -->'

    match_start = re.search(start_pattern, content)
    match_end = re.search(end_pattern, content)

    if match_start and match_end:
        grid_content = content[match_start.end():match_end.start()]
        cards = re.split(r'<!-- Card \d+ -->\s*', grid_content)
        cards = [c for c in cards if c.strip() != '']

        new_card = f"""
                    <div class="bg-white/60 dark:bg-white/5 border border-zinc-200 dark:border-white/10 backdrop-blur-md rounded-2xl overflow-hidden hover:-translate-y-2 hover:shadow-2xl hover:shadow-gold-500/5 hover:border-gold-500/30 transition-all duration-300 flex flex-col justify-between min-h-[440px] group" x-transition >
                        <div class="relative w-full h-48 overflow-hidden bg-zinc-900 border-b border-zinc-200 dark:border-white/5">
                            <img src="{args.img}" alt="Miniatura" class="w-full h-full object-cover transition-all duration-500 group-hover:scale-105 brightness-[1.1] contrast-[1.02] md:brightness-100 md:contrast-100" loading="lazy" decoding="async">
                        </div>
                        <div class="p-6 flex-grow flex flex-col justify-between space-y-4">
                            <div class="space-y-3">
                                <div class="flex items-center justify-between">
                                    <div class="inline-flex items-center space-x-1.5 px-2 py-0.5 bg-zinc-1550/60 dark:bg-white/5 border border-zinc-200 dark:border-white/10 rounded-md text-[9px] font-mono font-medium text-zinc-600 dark:text-zinc-300 uppercase tracking-wider">
                                        <span class="h-1.5 w-1.5 rounded-full bg-red-500 animate-pulse"></span>
                                        <span>{args.tag}</span>
                                    </div>
                                    <span class="text-[9px] text-zinc-500 font-mono">{args.date}</span>
                                </div>
                                <h3 class="font-playfair text-base sm:text-lg font-bold text-zinc-900 dark:text-white group-hover:text-gold-600 dark:group-hover:text-gold-400 transition-colors leading-snug">
                                    "{args.title}"
                                </h3>
                                <p class="text-xs text-zinc-600 dark:text-zinc-400 font-light leading-relaxed">
                                    {args.desc}
                                </p>
                            </div>
                            <div class="pt-4 border-t border-zinc-200 dark:border-white/5">
                                <a href="{args.url}" class="inline-flex items-center text-xs font-semibold tracking-wider text-zinc-700 hover:text-gold-600 dark:text-zinc-300 dark:hover:text-gold-400 transition-colors uppercase">
                                    Iniciar Autópsia &nbsp;➔
                                </a>
                            </div>
                        </div>
                    </div>
        """

        cards.insert(0, new_card.strip() + "\n\n")
        
        # Now pop the 6th card and add it to the thumbnails
        popped_card = cards.pop() if len(cards) > 6 else None
        
        new_grid_content = ""
        for i, c in enumerate(cards):
            # The first card gets special col-span and larger image
            c = re.sub(r'\s*md:col-span-2\s+lg:col-span-[23]\s*', ' ', c)
            c = c.replace('h-64 md:h-[22rem]', 'h-48')
            
            if i == 0:
                c = c.replace('class="bg-white/60', 'class="md:col-span-2 lg:col-span-2 bg-white/60')
                c = c.replace('h-48', 'h-64 md:h-[22rem]')
                
            new_grid_content += f"<!-- Card {i+1} -->\n{c.strip()}\n\n"

        content = content[:match_start.end()] + new_grid_content + content[match_end.start():]
        print("Main cards updated.")
        
        # 3. If there is a popped card, extract its details and add it to the thumbnails
        if popped_card:
            print("Extracting popped card details for thumbnail integration...")
            url_match = re.search(r'a href="([^"]+)"', popped_card)
            img_match = re.search(r'img src="([^"]+)"', popped_card)
            title_match = re.search(r'<h3[^>]*>\s*"(.*?)"\s*</h3>', popped_card, re.DOTALL)
            desc_match = re.search(r'<p[^>]*>\s*(.*?)\s*</p>', popped_card, re.DOTALL)
            
            if url_match and img_match and title_match and desc_match:
                popped_url = url_match.group(1)
                popped_img = img_match.group(1)
                popped_title = title_match.group(1).strip()
                popped_desc = desc_match.group(1).strip()
                
                start_thumb = r'<!-- Grid de Miniaturas -->\s*<div class="grid grid-cols-1 md:grid-cols-2 gap-4">\s*'
                end_thumb = r'\s*</div>\s*</section>\s*<!-- SEÇÃO 1: AUTÓPSIA DA MÍDIA -->'

                m_start_thumb = re.search(start_thumb, content)
                m_end_thumb = re.search(end_thumb, content)

                if m_start_thumb and m_end_thumb:
                    thumb_content = content[m_start_thumb.end():m_end_thumb.start()]
                    thumbs = re.split(r'<!-- Item \d+ -->\s*', thumb_content)
                    thumbs = [t for t in thumbs if t.strip() != '']

                    new_thumb = f"""
                    <a href="{popped_url}" class="flex items-center p-4 bg-white/60 dark:bg-white/5 border border-zinc-200 dark:border-white/10 backdrop-blur-md rounded-xl hover:-translate-y-1 hover:shadow-lg hover:border-gold-500/30 transition-all duration-300 group" >
                        <div class="flex-shrink-0 pr-4">
                            <img src="{popped_img}" alt="Miniatura" class="w-16 h-16 md:w-20 md:h-20 object-cover rounded-lg group-hover:scale-105 transition-all duration-300" loading="lazy">
                        </div>
                        <div class="flex-grow">
                            <h4 class="font-playfair text-sm md:text-base font-bold text-zinc-900 dark:text-white group-hover:text-gold-600 dark:group-hover:text-gold-400 transition-colors leading-snug">
                                {popped_title}
                            </h4>
                            <p class="text-[11px] md:text-xs text-zinc-600 dark:text-zinc-400 font-light mt-2 line-clamp-2">
                                {popped_desc}
                            </p>
                        </div>
                    </a>
                    """

                    thumbs.insert(0, new_thumb.strip() + "\n\n")
                    thumbs = thumbs[:6]
                    
                    new_thumb_grid = ""
                    for i, t in enumerate(thumbs):
                        new_thumb_grid += f"<!-- Item {i+1} -->\n{t.strip()}\n\n"

                    content = content[:m_start_thumb.end()] + new_thumb_grid + content[m_end_thumb.start():]
                    print("Thumbnails updated with popped card.")
                
    else:
        print("Could not find radar grid.")

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("Deployment script executed successfully! index.html is fully updated.")

if __name__ == '__main__':
    main()
