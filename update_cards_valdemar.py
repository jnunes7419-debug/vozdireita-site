import re

with open('d:\\direita_intelectual\\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Define the start of the grid
grid_start_str = 'id="radar-grid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">'
grid_start = content.find(grid_start_str)

# The grid ends right before:
grid_end_str = '                                    </div>\n            </section>\n\n\n            <!-- SEÇÃO MAIS ARTIGOS (MINIATURAS) -->'
post_grid_idx = content.find(grid_end_str, grid_start)

if grid_start == -1:
    print("Grid start not found")
    exit(1)
if post_grid_idx == -1:
    print("Grid end not found")
    grid_end_str2 = '</div>\n            </section>'
    post_grid_idx = content.find(grid_end_str2, grid_start)
    if post_grid_idx == -1:
        print("Grid end completely not found")
        exit(1)

grid_content = content[grid_start + len(grid_start_str):post_grid_idx]

parts = grid_content.split('<!-- Card')
prefix = parts[0]
cards_raw = parts[1:]

cards = []
for c in cards_raw:
    card_body = re.sub(r'^\s*\d+\s*(?:\([^)]+\))?\s*-->\s*', '', c, count=1)
    cards.append(card_body.strip())

if len(cards) > 0:
    cards[0] = cards[0].replace('md:col-span-2 lg:col-span-2 ', '')
    cards[0] = cards[0].replace('h-64 md:h-[22rem]', 'h-48')

new_card = """
<div class="md:col-span-2 lg:col-span-2 bg-white/60 dark:bg-white/5 border border-zinc-200 dark:border-white/10 backdrop-blur-md rounded-2xl overflow-hidden hover:-translate-y-2 hover:shadow-2xl hover:shadow-gold-500/5 hover:border-gold-500/30 transition-all duration-300 flex flex-col justify-between min-h-[440px] group" x-transition>
    <div class="relative w-full h-64 md:h-[22rem] overflow-hidden bg-zinc-900 border-b border-zinc-200 dark:border-white/5">
        <img src="assets/capa_valdemar.png" alt="Miniatura Bloqueio Valdemar" class="w-full h-full object-cover object-top transition-all duration-500 group-hover:scale-105 brightness-[1.1] contrast-[1.02] md:brightness-100 md:contrast-100" loading="lazy" decoding="async">
    </div>
    <div class="p-6 flex-grow flex flex-col justify-between space-y-4">
        <div class="space-y-3">
            <div class="flex items-center justify-between">
                <div class="inline-flex items-center space-x-1.5 px-2 py-0.5 bg-zinc-1550/60 dark:bg-white/5 border border-zinc-200 dark:border-white/10 rounded-md text-[9px] font-mono font-medium text-zinc-600 dark:text-zinc-300 uppercase tracking-wider">
                    <span class="h-1.5 w-1.5 rounded-full bg-red-500 animate-pulse"></span>
                    <span>INTERCEPTADO | CARTA CAPITAL</span>
                </div>
                <span class="text-[9px] text-zinc-500 font-mono">10 de Julho, 2026</span>
            </div>
            <h3 class="font-playfair text-base sm:text-lg font-bold text-zinc-900 dark:text-white group-hover:text-gold-600 dark:group-hover:text-gold-400 transition-colors leading-snug">
                "Dino suspeita de irregularidade e manda bloquear R$ 119 milhões de Valdemar"
            </h3>
            <p class="text-xs text-zinc-600 dark:text-zinc-400 font-light leading-relaxed">
                Como a mídia de esquerda criminaliza a oposição e normaliza bloqueios milionários sob o verniz da Justiça.
            </p>
        </div>
        <div class="pt-4 border-t border-zinc-200 dark:border-white/5">
            <a href="analise-cartacapital-valdemar.html" class="inline-flex items-center text-xs font-semibold tracking-wider text-zinc-700 hover:text-gold-600 dark:text-zinc-300 dark:hover:text-gold-400 transition-colors uppercase">
                Iniciar Autópsia &nbsp;➔
            </a>
        </div>
    </div>
</div>
"""

cards.insert(0, new_card.strip())

cards = cards[:8]

new_grid_content = prefix
for i, c in enumerate(cards):
    new_grid_content += f"\n<!-- Card {i+1} -->\n{c}\n"

new_content = content[:grid_start + len(grid_start_str)] + new_grid_content + '\n' + content[post_grid_idx:]

with open('d:\\direita_intelectual\\index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
print("Updated Valdemar successfully")
