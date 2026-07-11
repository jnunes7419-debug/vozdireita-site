import re

def main():
    file_path = 'd:\\direita_intelectual\\index.html'
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Locate the radar grid
    start_pattern = r'<div id="radar-grid".*?>\s*'
    end_pattern = r'\s*</div>\s*</section>\s*<!-- SEÇÃO MAIS ARTIGOS \(MINIATURAS\) -->'

    match_start = re.search(start_pattern, content)
    match_end = re.search(end_pattern, content)
    
    if not match_start or not match_end:
        print("Could not find radar grid.")
        return

    grid_content = content[match_start.end():match_end.start()]

    # Split by <!-- Card X -->
    cards = re.split(r'<!-- Card \d+ -->\s*', grid_content)
    cards = [c for c in cards if c.strip() != '']
    
    # The old Card 1 has the large classes. We need to remove them so it becomes a normal card.
    if len(cards) > 0:
        old_card1 = cards[0]
        # Remove col-span classes
        old_card1 = old_card1.replace('md:col-span-2 lg:col-span-2 ', '')
        # Change height class
        old_card1 = old_card1.replace('h-64 md:h-[22rem]', 'h-48')
        cards[0] = old_card1

    # Now create the new Card 1
    new_card_html = """
<div class="md:col-span-2 lg:col-span-2 bg-white/60 dark:bg-white/5 border border-zinc-200 dark:border-white/10 backdrop-blur-md rounded-2xl overflow-hidden hover:-translate-y-2 hover:shadow-2xl hover:shadow-gold-500/5 hover:border-gold-500/30 transition-all duration-300 flex flex-col justify-between min-h-[440px] group" x-transition>
    <div class="relative w-full h-64 md:h-[22rem] overflow-hidden bg-zinc-900 border-b border-zinc-200 dark:border-white/5">
        <img src="assets/trump_lula_diplomacy_1783795810788.png" alt="Miniatura Geopolítica" class="w-full h-full object-cover object-top transition-all duration-500 group-hover:scale-105 brightness-[1.1] contrast-[1.02] md:brightness-100 md:contrast-100" loading="lazy" decoding="async">
    </div>
    <div class="p-6 flex-grow flex flex-col justify-between space-y-4">
        <div class="space-y-3">
            <div class="flex items-center justify-between">
                <div class="inline-flex items-center space-x-1.5 px-2 py-0.5 bg-zinc-1550/60 dark:bg-white/5 border border-zinc-200 dark:border-white/10 rounded-md text-[9px] font-mono font-medium text-zinc-600 dark:text-zinc-300 uppercase tracking-wider">
                    <span class="h-1.5 w-1.5 rounded-full bg-red-500 animate-pulse"></span>
                    <span>INTERCEPTADO | METRÓPOLES</span>
                </div>
                <span class="text-[9px] text-zinc-500 font-mono">11 de Julho, 2026</span>
            </div>
            <h3 class="font-playfair text-base sm:text-lg font-bold text-zinc-900 dark:text-white group-hover:text-gold-600 dark:group-hover:text-gold-400 transition-colors leading-snug">
                "Governo Trump convida Brasil para evento contra a 'extrema esquerda'"
            </h3>
            <p class="text-xs text-zinc-600 dark:text-zinc-400 font-light leading-relaxed">
                A convocação de Washington expõe a hesitação da diplomacia brasileira e a escolha perigosa do governo frente ao extremismo transnacional.
            </p>
        </div>
        <div class="pt-4 border-t border-zinc-200 dark:border-white/5">
            <a href="analise-geopolitica-eua-brasil.html" class="inline-flex items-center text-xs font-semibold tracking-wider text-zinc-700 hover:text-gold-600 dark:text-zinc-300 dark:hover:text-gold-400 transition-colors uppercase">
                Iniciar Autópsia &nbsp;➔
            </a>
        </div>
    </div>
</div>
"""
    cards.insert(0, new_card_html.strip() + "\n\n")

    # Keep only the first 8 cards (estetica rule)
    cards = cards[:8]

    # Reconstruct the grid HTML with correct <!-- Card X -->
    new_grid_content = "\n"
    for i, c in enumerate(cards):
        new_grid_content += f"<!-- Card {i+1} -->\n{c.strip()}\n\n"

    new_content = content[:match_start.end()] + new_grid_content + content[match_end.start():]

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print("Radar grid updated successfully!")

if __name__ == '__main__':
    main()
