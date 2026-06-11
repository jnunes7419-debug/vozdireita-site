import re

def main():
    file_path = 'd:\\direita_intelectual\\index.html'
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    start_pattern = r'<!-- Grid de Miniaturas -->\s*<div class="grid grid-cols-1 md:grid-cols-2 gap-4">\s*'
    end_pattern = r'\s*</div>\s*</section>\s*<!-- SEÇÃO 1: AUTÓPSIA DA MÍDIA -->'

    match_start = re.search(start_pattern, content)
    match_end = re.search(end_pattern, content)
    
    if not match_start or not match_end:
        print("Could not find thumbnails grid.")
        return

    grid_content = content[match_start.end():match_end.start()]

    # We can split the cards. They start with <!-- Item X -->
    cards = re.split(r'<!-- Item \d+ -->\s*', grid_content)
    cards = [c for c in cards if c.strip() != '']
    
    new_card_html = """
                    <!-- Item 1 -->
                    <a href="analise-geopolitica-israel-ira.html" class="flex items-center p-4 bg-white/60 dark:bg-white/5 border border-zinc-200 dark:border-white/10 backdrop-blur-md rounded-xl hover:-translate-y-1 hover:shadow-lg hover:border-gold-500/30 transition-all duration-300 group" >
                        <div class="flex-shrink-0 pr-4">
                            <img src="assets/geopolitica_israel_ira.png" alt="Miniatura" class="w-16 h-16 md:w-20 md:h-20 object-cover rounded-lg group-hover:scale-105 transition-all duration-300" loading="lazy">
                        </div>
                        <div class="flex-grow">
                            <h4 class="font-playfair text-sm md:text-base font-bold text-zinc-900 dark:text-white group-hover:text-gold-600 dark:group-hover:text-gold-400 transition-colors leading-snug">
                                Conflito Israel e Irã: Inversão de Culpabilidade
                            </h4>
                            <p class="text-[11px] md:text-xs text-zinc-600 dark:text-zinc-400 font-light mt-2 line-clamp-2">
                                Como a mídia legitima o terrorismo sob disfarce de "apelo à paz".
                            </p>
                        </div>
                    </a>
"""

    cards.insert(0, new_card_html.strip() + "\n\n")

    # Keep only the first 6
    cards = cards[:6]

    # Reconstruct the grid HTML with correct <!-- Item X -->
    new_grid_content = ""
    for i, c in enumerate(cards):
        new_grid_content += f"<!-- Item {i+1} -->\n{c.strip()}\n\n"

    new_content = content[:match_start.end()] + new_grid_content + content[match_end.start():]

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print("Thumbnails updated successfully!")

if __name__ == '__main__':
    main()
