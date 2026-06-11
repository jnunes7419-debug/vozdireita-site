import re

with open('d:/direita_intelectual/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

grid_start_str = '<div id="radar-grid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">'
grid_start = content.find(grid_start_str)

if grid_start == -1:
    print("Grid not found")
    exit(1)

post_grid_idx = content.find('                                    </div>\n            </section>', grid_start)

if post_grid_idx == -1:
    print("Grid end not found")
    exit(1)

grid_content = content[grid_start + len(grid_start_str):post_grid_idx]

parts = grid_content.split('<!-- Card')
prefix = parts[0]
cards_raw = parts[1:]

cards = []
for c in cards_raw:
    card_body = re.sub(r'^\s*\d+\s*(?:\([^)]+\))?\s*-->\s*', '', c, count=1)
    cards.append(card_body)

new_card = """
<div class="md:col-span-2 lg:col-span-2 bg-white/60 dark:bg-white/5 border border-zinc-200 dark:border-white/10 backdrop-blur-md rounded-2xl overflow-hidden hover:-translate-y-2 hover:shadow-2xl hover:shadow-gold-500/5 hover:border-gold-500/30 transition-all duration-300 flex flex-col justify-between min-h-[440px] group" x-transition >
                        <div class="relative w-full h-64 md:h-[22rem] overflow-hidden bg-zinc-900 border-b border-zinc-200 dark:border-white/5">
                            <img src="assets/capa_fifa_trump.png" alt="Miniatura FIFA Trump" class="w-full h-full object-cover object-top transition-all duration-500 group-hover:scale-105 brightness-[1.1] contrast-[1.02] md:brightness-100 md:contrast-100" loading="lazy" decoding="async">
                        </div>
                        <div class="p-6 flex-grow flex flex-col justify-between space-y-4">
                            <div class="space-y-3">
                                <div class="flex items-center justify-between">
                                    <div class="inline-flex items-center space-x-1.5 px-2 py-0.5 bg-zinc-1550/60 dark:bg-white/5 border border-zinc-200 dark:border-white/10 rounded-md text-[9px] font-mono font-medium text-zinc-600 dark:text-zinc-300 uppercase tracking-wider">
                                        <span class="h-1.5 w-1.5 rounded-full bg-red-500 animate-pulse"></span>
                                        <span>INTERCEPTADO | G1 / L'ÉQUIPE</span>
                                    </div>
                                    <span class="text-[9px] text-zinc-500 font-mono">10 de Junho, 2026</span>
                                </div>
                                <h3 class="font-playfair text-base sm:text-lg font-bold text-zinc-900 dark:text-white group-hover:text-gold-600 dark:group-hover:text-gold-400 transition-colors leading-snug">
                                    "Gianni Infantino é chamado de fantoche de Trump no jornal L'Équipe"
                                </h3>
                                <p class="text-xs text-zinc-600 dark:text-zinc-400 font-light leading-relaxed">
                                    A Arma do Esporte: Como o globalismo instrumentaliza o futebol para demonizar a soberania e o controle de fronteiras.
                                </p>
                            </div>
                            <div class="pt-4 border-t border-zinc-200 dark:border-white/5">
                                <a href="analise-g1-fifa-trump.html" class="inline-flex items-center text-xs font-semibold tracking-wider text-zinc-700 hover:text-gold-600 dark:text-zinc-300 dark:hover:text-gold-400 transition-colors uppercase">
                                    Iniciar Autópsia &nbsp;➔
                                </a>
                            </div>
                        </div>
                    </div>
"""

cards.insert(0, new_card)

# Adjust max cards according to estetica.md = 8 cards max
if len(cards) > 8:
    cards = cards[:8]

# Ensure the first card takes col-span-2 as the layout implies
for i in range(len(cards)):
    cards[i] = re.sub(r'class="md:col-span-2 lg:col-span-2\s+', 'class="', cards[i])
    if i == 0:
        cards[i] = cards[i].replace('class="bg-white/60', 'class="md:col-span-2 lg:col-span-2 bg-white/60')
        cards[i] = cards[i].replace('h-48 overflow-hidden', 'h-64 md:h-[22rem] overflow-hidden')
    else:
        cards[i] = cards[i].replace('h-64 md:h-[22rem] overflow-hidden', 'h-48 overflow-hidden')

new_grid_content = prefix
for i, c in enumerate(cards):
    new_grid_content += f"<!-- Card {i+1} -->\n{c}\n"

new_content = content[:grid_start + len(grid_start_str)] + new_grid_content + content[post_grid_idx:]

with open('d:/direita_intelectual/index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Card FIFA adicionado com sucesso. Total cards:", len(cards))
