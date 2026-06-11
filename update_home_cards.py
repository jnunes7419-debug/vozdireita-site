import re

def main():
    file_path = 'd:\\direita_intelectual\\index.html'
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # The grid is between <div id="radar-grid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
    # and its closing </div> which is before <!-- SEÇÃO MAIS ARTIGOS (MINIATURAS) -->
    
    start_pattern = r'<div id="radar-grid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">\s*'
    end_pattern = r'\s*</div>\s*</section>\s*<!-- SEÇÃO MAIS ARTIGOS \(MINIATURAS\) -->'

    match_start = re.search(start_pattern, content)
    match_end = re.search(end_pattern, content)
    
    if not match_start or not match_end:
        print("Could not find radar grid.")
        return

    grid_content = content[match_start.end():match_end.start()]

    # We can split the cards. They start with <!-- Card X -->
    cards = re.split(r'<!-- Card \d+ -->\s*', grid_content)
    cards = [c for c in cards if c.strip() != '']
    
    new_card_html = """
                    <!-- Card 1 -->
                    <div class="bg-white/60 dark:bg-white/5 border border-zinc-200 dark:border-white/10 backdrop-blur-md rounded-2xl overflow-hidden hover:-translate-y-2 hover:shadow-2xl hover:shadow-gold-500/5 hover:border-gold-500/30 transition-all duration-300 flex flex-col justify-between min-h-[440px] group" x-transition >
                        
                        <!-- Container da Miniatura (Thumbnail) -->
                        <div class="relative w-full h-48 overflow-hidden bg-zinc-900 border-b border-zinc-200 dark:border-white/5">
                            <img src="assets/geopolitica_israel_ira.png" alt="Miniatura Conflito Israel Irã" class="w-full h-full object-cover transition-all duration-500 group-hover:scale-105 brightness-[1.1] contrast-[1.02] md:brightness-100 md:contrast-100" loading="lazy" decoding="async">
                        </div>

                        <!-- Corpo do Card -->
                        <div class="p-6 flex-grow flex flex-col justify-between space-y-4">
                            <div class="space-y-3">
                                <!-- Tag superior -->
                                <div class="flex items-center justify-between">
                                    <div class="inline-flex items-center space-x-1.5 px-2 py-0.5 bg-zinc-1550/60 dark:bg-white/5 border border-zinc-200 dark:border-white/10 rounded-md text-[9px] font-mono font-medium text-zinc-600 dark:text-zinc-300 uppercase tracking-wider">
                                        <span class="h-1.5 w-1.5 rounded-full bg-red-500 animate-pulse"></span>
                                        <span>INTERCEPTADO | G1 MUNDO</span>
                                    </div>
                                    <span class="text-[9px] text-zinc-500 font-mono">07 de Junho, 2026</span>
                                </div>

                                <!-- Manchete -->
                                <h3 class="font-playfair text-base sm:text-lg font-bold text-zinc-900 dark:text-white group-hover:text-gold-600 dark:group-hover:text-gold-400 transition-colors leading-snug">
                                    "Após bombardeios de Israel a Beirute, Irã lança mísseis..."
                                </h3>

                                <!-- Resumo tático -->
                                <p class="text-xs text-zinc-600 dark:text-zinc-400 font-light leading-relaxed">
                                    Como a mídia inverte a agressão primária e omite o financiamento do terrorismo para proteger o eixo anti-Ocidente.
                                </p>
                            </div>

                            <!-- Ação -->
                            <div class="pt-4 border-t border-zinc-200 dark:border-white/5">
                                <a href="analise-geopolitica-israel-ira.html" class="inline-flex items-center text-xs font-semibold tracking-wider text-zinc-700 hover:text-gold-600 dark:text-zinc-300 dark:hover:text-gold-400 transition-colors uppercase">
                                    Iniciar Autópsia &nbsp;➔
                                </a>
                            </div>
                        </div>

                    </div>
"""

    cards.insert(0, new_card_html.strip() + "\n\n")

    # Keep only the first 6
    cards = cards[:6]

    # Reconstruct the grid HTML with correct <!-- Card X -->
    new_grid_content = ""
    for i, c in enumerate(cards):
        # Remove any existing col-span modifiers and taller image classes
        c = re.sub(r'\s*md:col-span-2\s+lg:col-span-[23]\s*', ' ', c)
        c = c.replace('h-64 md:h-[22rem]', 'h-48')
        
        if i == 0:
            # Inject col-span-2 into the main div
            c = c.replace('class="bg-white/60', 'class="md:col-span-2 lg:col-span-2 bg-white/60')
            # Make image taller for the featured post
            c = c.replace('h-48', 'h-64 md:h-[22rem]')
            
        new_grid_content += f"<!-- Card {i+1} -->\n{c.strip()}\n\n"

    new_content = content[:match_start.end()] + new_grid_content + content[match_end.start():]

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print("Cards updated successfully!")

if __name__ == '__main__':
    main()
