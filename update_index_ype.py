import re

def update_index():
    file_path = 'd:\\direita_intelectual\\index.html'
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update the Search Array (x-data articles)
    new_article_obj = """        {
            title: 'Ypê e o Terror Burocrático: O uso da Anvisa',
            desc: 'A esquerda neototalitária instrumentaliza a Anvisa para impor a engenharia social coercitiva sobre a indústria nacional.',
            img: 'assets/sabotagem_ype.png',
            url: 'analise-g1-ype.html'
        },
"""
    # Insert right after `articles: [`
    articles_match = re.search(r'articles:\s*\[\s*', content)
    if articles_match:
        content = content[:articles_match.end()] + new_article_obj + content[articles_match.end():]

    # 2. Update the Grid
    start_pattern = r'<div id="radar-grid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">\s*'
    end_pattern = r'\s*</div>\s*</section>\s*<!-- SEÇÃO MAIS ARTIGOS \(MINIATURAS\) -->'

    match_start = re.search(start_pattern, content)
    match_end = re.search(end_pattern, content)
    
    if match_start and match_end:
        grid_content = content[match_start.end():match_end.start()]
        cards = re.split(r'<!-- Card \d+ -->\s*', grid_content)
        cards = [c for c in cards if c.strip() != '']
        
        # Remove md:col-span-2 and h-64 from the OLD first card
        if len(cards) > 0:
            cards[0] = cards[0].replace('md:col-span-2 lg:col-span-2 ', '')
            cards[0] = cards[0].replace('h-64 md:h-[22rem]', 'h-48')

        new_card = """
                    <div class="md:col-span-2 lg:col-span-2 bg-white/60 dark:bg-white/5 border border-zinc-200 dark:border-white/10 backdrop-blur-md rounded-2xl overflow-hidden hover:-translate-y-2 hover:shadow-2xl hover:shadow-gold-500/5 hover:border-gold-500/30 transition-all duration-300 flex flex-col justify-between min-h-[440px] group" x-transition >
                        <div class="relative w-full h-64 md:h-[22rem] overflow-hidden bg-zinc-900 border-b border-zinc-200 dark:border-white/5">
                            <img src="assets/sabotagem_ype.png" alt="Miniatura Ypê" class="w-full h-full object-cover transition-all duration-500 group-hover:scale-105 brightness-[1.1] contrast-[1.02] md:brightness-100 md:contrast-100" loading="lazy" decoding="async">
                        </div>
                        <div class="p-6 flex-grow flex flex-col justify-between space-y-4">
                            <div class="space-y-3">
                                <div class="flex items-center justify-between">
                                    <div class="inline-flex items-center space-x-1.5 px-2 py-0.5 bg-zinc-1550/60 dark:bg-white/5 border border-zinc-200 dark:border-white/10 rounded-md text-[9px] font-mono font-medium text-zinc-600 dark:text-zinc-300 uppercase tracking-wider">
                                        <span class="h-1.5 w-1.5 rounded-full bg-red-500 animate-pulse"></span>
                                        <span>INTERCEPTADO | G1</span>
                                    </div>
                                    <span class="text-[9px] text-zinc-500 font-mono">12 de Maio, 2026</span>
                                </div>
                                <h3 class="font-playfair text-base sm:text-lg font-bold text-zinc-900 dark:text-white group-hover:text-gold-600 dark:group-hover:text-gold-400 transition-colors leading-snug">
                                    "Ypê: final 1 no lote identifica produtos feitos em Amparo..."
                                </h3>
                                <p class="text-xs text-zinc-600 dark:text-zinc-400 font-light leading-relaxed">
                                    Como a esquerda neototalitária instrumentaliza a Anvisa para impor a engenharia social coercitiva e asfixiar a indústria nacional.
                                </p>
                            </div>
                            <div class="pt-4 border-t border-zinc-200 dark:border-white/5">
                                <a href="analise-g1-ype.html" class="inline-flex items-center text-xs font-semibold tracking-wider text-zinc-700 hover:text-gold-600 dark:text-zinc-300 dark:hover:text-gold-400 transition-colors uppercase">
                                    Iniciar Autópsia &nbsp;➔
                                </a>
                            </div>
                        </div>
                    </div>
        """
        
        cards.insert(0, new_card.strip())
        
        # Keep exactly 7 cards (drop the last one, which was STF)
        cards = cards[:7]
        
        # The user's exact praised structure had `hidden md:flex` on Card 6 (index 5)
        # So we should make sure Card 6 has it, or just let it flow natively if there are 7 cards.
        # Actually, if there are 7 cards, they all fit perfectly (2 top, 4 bottom = 7).
        # Wait, 1 large = 2 slots. + 2 small = 4 slots (1 row).
        # 4 small on bottom = 4 slots (1 row).
        # Total = 8 slots! So 1 Large + 6 Small = 7 Cards total!
        # So having 7 cards perfectly fills an 8-slot grid (since 1 is double-wide).
        
        new_grid_content = ""
        for i, c in enumerate(cards):
            new_grid_content += f"<!-- Card {i+1} -->\n{c.strip()}\n\n"

        content = content[:match_start.end()] + new_grid_content + content[match_end.start():]
        
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("Index updated with new Ypê article successfully!")

if __name__ == '__main__':
    update_index()
