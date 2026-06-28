import re
import json

def update_cards():
    file_path = 'd:\\direita_intelectual\\index.html'
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update Radar de Narrativas (radar-grid)
    start_pattern = r'<div id="radar-grid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">\s*'
    end_pattern = r'\s*</div>\s*</section>\s*<!-- SEÇÃO MAIS ARTIGOS \(MINIATURAS\) -->'

    match_start = re.search(start_pattern, content)
    match_end = re.search(end_pattern, content)
    
    if not match_start or not match_end:
        print("Could not find radar-grid.")
        return

    grid_content = content[match_start.end():match_end.start()]

    # We can split the cards. They start with <!-- Card X -->
    cards = re.split(r'<!-- Card \d+ -->\s*', grid_content)
    cards = [c for c in cards if c.strip() != '']
    
    new_card_html = """
<div class="md:col-span-2 lg:col-span-2 bg-white/60 dark:bg-white/5 border border-zinc-200 dark:border-white/10 backdrop-blur-md rounded-2xl overflow-hidden hover:-translate-y-2 hover:shadow-2xl hover:shadow-gold-500/5 hover:border-gold-500/30 transition-all duration-300 flex flex-col justify-between min-h-[440px] group" x-transition >
                        <div class="relative w-full h-64 md:h-[22rem] overflow-hidden bg-zinc-900 border-b border-zinc-200 dark:border-white/5">
                            <img src="assets/caso_master_autopsia.png" alt="Miniatura Caso Master" class="w-full h-full object-cover object-top transition-all duration-500 group-hover:scale-105 brightness-[1.1] contrast-[1.02] md:brightness-100 md:contrast-100" loading="lazy" decoding="async">
                        </div>
                        <div class="p-6 flex-grow flex flex-col justify-between space-y-4">
                            <div class="space-y-3">
                                <div class="flex items-center justify-between">
                                    <div class="inline-flex items-center space-x-1.5 px-2 py-0.5 bg-zinc-1550/60 dark:bg-white/5 border border-zinc-200 dark:border-white/10 rounded-md text-[9px] font-mono font-medium text-zinc-600 dark:text-zinc-300 uppercase tracking-wider">
                                        <span class="h-1.5 w-1.5 rounded-full bg-red-500 animate-pulse"></span>
                                        <span>INTERCEPTADO | G1</span>
                                    </div>
                                    <span class="text-[9px] text-zinc-500 font-mono">11 de Junho, 2026</span>
                                </div>
                                <h3 class="font-playfair text-base sm:text-lg font-bold text-zinc-900 dark:text-white group-hover:text-gold-600 dark:group-hover:text-gold-400 transition-colors leading-snug">
                                    "A Justiça Seletiva e o Caso Master: PF rejeita 2ª proposta de delação"
                                </h3>
                                <p class="text-xs text-zinc-600 dark:text-zinc-400 font-light leading-relaxed">
                                    Aparelhamento Jurídico: Como as manobras no judiciário e a rejeição de delações operam a proteção seletiva e a manutenção do ecossistema corporativo.
                                </p>
                            </div>
                            <div class="pt-4 border-t border-zinc-200 dark:border-white/5">
                                <a href="analise-g1-master.html" class="inline-flex items-center text-xs font-semibold tracking-wider text-zinc-700 hover:text-gold-600 dark:text-zinc-300 dark:hover:text-gold-400 transition-colors uppercase">
                                    Iniciar Autópsia &nbsp;➔
                                </a>
                            </div>
                        </div>
                    </div>
"""

    cards.insert(0, new_card_html.strip() + "\n\n")

    # Keep only the first 8 cards
    cards = cards[:8]

    # Reconstruct the grid HTML with correct <!-- Card X -->
    new_grid_content = ""
    for i, c in enumerate(cards):
        # The new Card 1 already has the md:col-span-2 lg:col-span-2
        # But if it's card 2, we need to remove it if it was the old card 1
        if i > 0:
            c = c.replace('md:col-span-2 lg:col-span-2 ', '')
            c = c.replace('h-64 md:h-[22rem]', 'h-48')
            
        new_grid_content += f"<!-- Card {i+1} -->\n{c.strip()}\n\n\n"

    new_content = content[:match_start.end()] + new_grid_content + content[match_end.start():]
    
    # 2. Update the Alpine.js array for the search
    # Find articles: [
    articles_start = r'articles: \['
    match_articles = re.search(articles_start, new_content)
    if match_articles:
        new_article = """
        {
            title: 'A Justiça Seletiva e o Caso Master',
            desc: 'Aparelhamento Jurídico: Como as manobras no judiciário e a rejeição de delações operam a proteção seletiva.',
            img: 'assets/caso_master_autopsia.png',
            url: 'analise-g1-master.html'
        },"""
        new_content = new_content[:match_articles.end()] + new_article + new_content[match_articles.end():]

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print("Cards updated successfully!")

if __name__ == '__main__':
    update_cards()
