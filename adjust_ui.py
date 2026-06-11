import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Hide cards 4, 5, 6 on mobile in the Radar section
# We'll find <!-- Card X --> and add 'hidden md:flex' if X > 3
radar_grid_start = content.find('<!-- SEÇÃO RADAR DE NARRATIVAS')
radar_grid_end = content.find('<!-- SEÇÃO MAIS ARTIGOS')
if radar_grid_start != -1 and radar_grid_end != -1:
    radar_content = content[radar_grid_start:radar_grid_end]
    
    # Let's find all cards and replace their classes
    for i in range(4, 9): # 4 to 8
        marker = f'<!-- Card {i} -->\n                    <div class="'
        if marker in radar_content:
            # check if hidden md:flex is already there
            idx = radar_content.find(marker)
            if 'hidden md:flex' not in radar_content[idx:idx+200]:
                radar_content = radar_content.replace(marker, marker + 'hidden md:flex ')

    content = content[:radar_grid_start] + radar_content + content[radar_grid_end:]

# 2. Rebuild the "Mais Artigos" section
mais_artigos_start = content.find('<!-- SEÇÃO MAIS ARTIGOS (MINIATURAS) -->')
mais_artigos_end = content.find('<!-- SEÇÃO 1: AUTÓPSIA DA MÍDIA -->')

if mais_artigos_start != -1 and mais_artigos_end != -1:
    new_mais_artigos = """<!-- SEÇÃO MAIS ARTIGOS (MINIATURAS) -->
            <section id="mais-artigos" class="py-8 max-w-7xl mx-auto px-6 relative border-b border-zinc-200 dark:border-zinc-500/10">
                <!-- Cabeçalho da Seção -->
                <div class="mb-8 border-b border-zinc-200 dark:border-white/10 pb-4">
                    <h3 class="text-xl md:text-2xl font-bold tracking-tight font-playfair text-zinc-900 dark:text-white">
                        Mais Artigos
                    </h3>
                </div>

                <!-- Grid de Miniaturas -->
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    
                    <!-- Item 1 -->
                    <a href="analise-g1-homeschooling.html" class="flex items-center p-4 bg-white/60 dark:bg-white/5 border border-zinc-200 dark:border-white/10 backdrop-blur-md rounded-xl hover:-translate-y-1 hover:shadow-lg hover:border-gold-500/30 transition-all duration-300 group" x-show="searchQuery === '' || $el.textContent.toLowerCase().includes(searchQuery.toLowerCase())">
                        <div class="flex-shrink-0 pr-4">
                            <img src="assets/homeschooling_condenacao.png" alt="Miniatura" class="w-16 h-16 md:w-20 md:h-20 object-cover rounded-lg group-hover:scale-105 transition-all duration-300" loading="lazy">
                        </div>
                        <div class="flex-grow">
                            <h4 class="font-playfair text-sm md:text-base font-bold text-zinc-900 dark:text-white group-hover:text-gold-600 dark:group-hover:text-gold-400 transition-colors leading-snug">
                                Pais são condenados por homeschooling em SP
                            </h4>
                            <p class="text-[11px] md:text-xs text-zinc-600 dark:text-zinc-400 font-light mt-2 line-clamp-2">
                                A criminalização do ensino domiciliar através da Engenharia Social Coercitiva.
                            </p>
                        </div>
                    </a>

                    <!-- Item 2 -->
                    <a href="analise-oglobo-messias.html" class="flex items-center p-4 bg-white/60 dark:bg-white/5 border border-zinc-200 dark:border-white/10 backdrop-blur-md rounded-xl hover:-translate-y-1 hover:shadow-lg hover:border-gold-500/30 transition-all duration-300 group" x-show="searchQuery === '' || $el.textContent.toLowerCase().includes(searchQuery.toLowerCase())">
                        <div class="flex-shrink-0 pr-4">
                            <img src="assets/messias_marcha.png" alt="Miniatura" class="w-16 h-16 md:w-20 md:h-20 object-cover rounded-lg group-hover:scale-105 transition-all duration-300" loading="lazy">
                        </div>
                        <div class="flex-grow">
                            <h4 class="font-playfair text-sm md:text-base font-bold text-zinc-900 dark:text-white group-hover:text-gold-600 dark:group-hover:text-gold-400 transition-colors leading-snug">
                                Messias rebate discurso de Flávio na Marcha
                            </h4>
                            <p class="text-[11px] md:text-xs text-zinc-600 dark:text-zinc-400 font-light mt-2 line-clamp-2">
                                Como a mídia blinda o governo e tenta interditar a indignação cristã.
                            </p>
                        </div>
                    </a>

                    <!-- Item 3 -->
                    <a href="analise-rodaviva-bolsonaro.html" class="flex items-center p-4 bg-white/60 dark:bg-white/5 border border-zinc-200 dark:border-white/10 backdrop-blur-md rounded-xl hover:-translate-y-1 hover:shadow-lg hover:border-gold-500/30 transition-all duration-300 group" x-show="searchQuery === '' || $el.textContent.toLowerCase().includes(searchQuery.toLowerCase())">
                        <div class="flex-shrink-0 pr-4">
                            <img src="assets/rodaviva_lobos.png" alt="Miniatura" class="w-16 h-16 md:w-20 md:h-20 object-cover rounded-lg group-hover:scale-105 transition-all duration-300" loading="lazy">
                        </div>
                        <div class="flex-grow">
                            <h4 class="font-playfair text-sm md:text-base font-bold text-zinc-900 dark:text-white group-hover:text-gold-600 dark:group-hover:text-gold-400 transition-colors leading-snug">
                                A Sabotagem Editorial do Roda Viva 2018
                            </h4>
                            <p class="text-[11px] md:text-xs text-zinc-600 dark:text-zinc-400 font-light mt-2 line-clamp-2">
                                Os bastidores das táticas inquisitoriais de debate.
                            </p>
                        </div>
                    </a>

                    <!-- Item 4 -->
                    <a href="analise-uol-terrorismo.html" class="flex items-center p-4 bg-white/60 dark:bg-white/5 border border-zinc-200 dark:border-white/10 backdrop-blur-md rounded-xl hover:-translate-y-1 hover:shadow-lg hover:border-gold-500/30 transition-all duration-300 group" x-show="searchQuery === '' || $el.textContent.toLowerCase().includes(searchQuery.toLowerCase())">
                        <div class="flex-shrink-0 pr-4">
                            <img src="assets/seguranca_rj.png" alt="Miniatura" class="w-16 h-16 md:w-20 md:h-20 object-cover rounded-lg group-hover:scale-105 transition-all duration-300" loading="lazy">
                        </div>
                        <div class="flex-grow">
                            <h4 class="font-playfair text-sm md:text-base font-bold text-zinc-900 dark:text-white group-hover:text-gold-600 dark:group-hover:text-gold-400 transition-colors leading-snug">
                                Feitiço do terrorismo e Flávio Bolsonaro
                            </h4>
                            <p class="text-[11px] md:text-xs text-zinc-600 dark:text-zinc-400 font-light mt-2 line-clamp-2">
                                A esquerda neototalitária tenta criminalizar a oposição.
                            </p>
                        </div>
                    </a>

                    <!-- Item 5 -->
                    <a href="analise-g1-monique.html" class="flex items-center p-4 bg-white/60 dark:bg-white/5 border border-zinc-200 dark:border-white/10 backdrop-blur-md rounded-xl hover:-translate-y-1 hover:shadow-lg hover:border-gold-500/30 transition-all duration-300 group" x-show="searchQuery === '' || $el.textContent.toLowerCase().includes(searchQuery.toLowerCase())">
                        <div class="flex-shrink-0 pr-4">
                            <img src="assets/monique_liberada.png" alt="Miniatura" class="w-16 h-16 md:w-20 md:h-20 object-cover rounded-lg group-hover:scale-105 transition-all duration-300" loading="lazy">
                        </div>
                        <div class="flex-grow">
                            <h4 class="font-playfair text-sm md:text-base font-bold text-zinc-900 dark:text-white group-hover:text-gold-600 dark:group-hover:text-gold-400 transition-colors leading-snug">
                                Decisão libera Monique Medeiros da prisão
                            </h4>
                            <p class="text-[11px] md:text-xs text-zinc-600 dark:text-zinc-400 font-light mt-2 line-clamp-2">
                                O progressismo autoritário e a anestesia da opinião pública.
                            </p>
                        </div>
                    </a>

                    <!-- Item 6 -->
                    <a href="analise-oglobo-rosa.html" class="flex items-center p-4 bg-white/60 dark:bg-white/5 border border-zinc-200 dark:border-white/10 backdrop-blur-md rounded-xl hover:-translate-y-1 hover:shadow-lg hover:border-gold-500/30 transition-all duration-300 group" x-show="searchQuery === '' || $el.textContent.toLowerCase().includes(searchQuery.toLowerCase())">
                        <div class="flex-shrink-0 pr-4">
                            <img src="assets/tornozeleira_rosa.png" alt="Miniatura" class="w-16 h-16 md:w-20 md:h-20 object-cover rounded-lg group-hover:scale-105 transition-all duration-300" loading="lazy">
                        </div>
                        <div class="flex-grow">
                            <h4 class="font-playfair text-sm md:text-base font-bold text-zinc-900 dark:text-white group-hover:text-gold-600 dark:group-hover:text-gold-400 transition-colors leading-snug">
                                A Armadilha do Cavalo de Troia no PL
                            </h4>
                            <p class="text-[11px] md:text-xs text-zinc-600 dark:text-zinc-400 font-light mt-2 line-clamp-2">
                                Como a tornozeleira rosa cinde a base conservadora.
                            </p>
                        </div>
                    </a>

                </div>
            </section>
            
"""
    content = content[:mais_artigos_start] + new_mais_artigos + content[mais_artigos_end:]
    
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Adjustments applied.")
