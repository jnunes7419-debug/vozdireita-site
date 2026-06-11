import io

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

insertion_marker = "            <!-- SEÇÃO 1: AUTÓPSIA DA MÍDIA -->"

new_section = """
            <!-- SEÇÃO MAIS ARTIGOS (MINIATURAS) -->
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
                    <a href="#" class="flex items-center justify-between p-4 bg-white/60 dark:bg-white/5 border border-zinc-200 dark:border-white/10 backdrop-blur-md rounded-xl hover:-translate-y-1 hover:shadow-lg hover:border-gold-500/30 transition-all duration-300 group" x-show="searchQuery === '' || $el.textContent.toLowerCase().includes(searchQuery.toLowerCase())">
                        <div class="pr-4 flex-grow">
                            <h4 class="font-playfair text-sm md:text-base font-bold text-zinc-900 dark:text-white group-hover:text-gold-600 dark:group-hover:text-gold-400 transition-colors leading-snug">
                                "A Criminalização da Liberdade de Expressão no Meio Digital"
                            </h4>
                            <p class="text-[11px] md:text-xs text-zinc-600 dark:text-zinc-400 font-light mt-2 line-clamp-2">
                                Como a censura é terceirizada para agências de checagem.
                            </p>
                        </div>
                        <div class="flex-shrink-0">
                            <img src="assets/seguranca_rj.png" alt="Miniatura" class="w-16 h-16 md:w-20 md:h-20 object-cover rounded-lg group-hover:scale-105 transition-all duration-300" loading="lazy">
                        </div>
                    </a>

                    <!-- Item 2 -->
                    <a href="#" class="flex items-center justify-between p-4 bg-white/60 dark:bg-white/5 border border-zinc-200 dark:border-white/10 backdrop-blur-md rounded-xl hover:-translate-y-1 hover:shadow-lg hover:border-gold-500/30 transition-all duration-300 group" x-show="searchQuery === '' || $el.textContent.toLowerCase().includes(searchQuery.toLowerCase())">
                        <div class="pr-4 flex-grow">
                            <h4 class="font-playfair text-sm md:text-base font-bold text-zinc-900 dark:text-white group-hover:text-gold-600 dark:group-hover:text-gold-400 transition-colors leading-snug">
                                "O Falso Consenso e o Monitoramento de Dados"
                            </h4>
                            <p class="text-[11px] md:text-xs text-zinc-600 dark:text-zinc-400 font-light mt-2 line-clamp-2">
                                A ilusão de escolha e o direcionamento algorítmico do cidadão.
                            </p>
                        </div>
                        <div class="flex-shrink-0">
                            <img src="assets/rodaviva_lobos.png" alt="Miniatura" class="w-16 h-16 md:w-20 md:h-20 object-cover rounded-lg group-hover:scale-105 transition-all duration-300" loading="lazy">
                        </div>
                    </a>

                    <!-- Item 3 -->
                    <a href="#" class="flex items-center justify-between p-4 bg-white/60 dark:bg-white/5 border border-zinc-200 dark:border-white/10 backdrop-blur-md rounded-xl hover:-translate-y-1 hover:shadow-lg hover:border-gold-500/30 transition-all duration-300 group" x-show="searchQuery === '' || $el.textContent.toLowerCase().includes(searchQuery.toLowerCase())">
                        <div class="pr-4 flex-grow">
                            <h4 class="font-playfair text-sm md:text-base font-bold text-zinc-900 dark:text-white group-hover:text-gold-600 dark:group-hover:text-gold-400 transition-colors leading-snug">
                                "A Desconstrução da Família Através das Pautas ESG"
                            </h4>
                            <p class="text-[11px] md:text-xs text-zinc-600 dark:text-zinc-400 font-light mt-2 line-clamp-2">
                                Engenharia social corporativa como ferramenta de desestabilização.
                            </p>
                        </div>
                        <div class="flex-shrink-0">
                            <img src="assets/tornozeleira_rosa.png" alt="Miniatura" class="w-16 h-16 md:w-20 md:h-20 object-cover rounded-lg group-hover:scale-105 transition-all duration-300" loading="lazy">
                        </div>
                    </a>

                    <!-- Item 4 -->
                    <a href="#" class="flex items-center justify-between p-4 bg-white/60 dark:bg-white/5 border border-zinc-200 dark:border-white/10 backdrop-blur-md rounded-xl hover:-translate-y-1 hover:shadow-lg hover:border-gold-500/30 transition-all duration-300 group" x-show="searchQuery === '' || $el.textContent.toLowerCase().includes(searchQuery.toLowerCase())">
                        <div class="pr-4 flex-grow">
                            <h4 class="font-playfair text-sm md:text-base font-bold text-zinc-900 dark:text-white group-hover:text-gold-600 dark:group-hover:text-gold-400 transition-colors leading-snug">
                                "Hegemonia Acadêmica: O Aparelhamento nas Faculdades"
                            </h4>
                            <p class="text-[11px] md:text-xs text-zinc-600 dark:text-zinc-400 font-light mt-2 line-clamp-2">
                                Como a intelectualidade foi cooptada pelo progressismo militante.
                            </p>
                        </div>
                        <div class="flex-shrink-0">
                            <img src="assets/homeschooling_condenacao.png" alt="Miniatura" class="w-16 h-16 md:w-20 md:h-20 object-cover rounded-lg group-hover:scale-105 transition-all duration-300" loading="lazy">
                        </div>
                    </a>

                    <!-- Item 5 -->
                    <a href="#" class="flex items-center justify-between p-4 bg-white/60 dark:bg-white/5 border border-zinc-200 dark:border-white/10 backdrop-blur-md rounded-xl hover:-translate-y-1 hover:shadow-lg hover:border-gold-500/30 transition-all duration-300 group" x-show="searchQuery === '' || $el.textContent.toLowerCase().includes(searchQuery.toLowerCase())">
                        <div class="pr-4 flex-grow">
                            <h4 class="font-playfair text-sm md:text-base font-bold text-zinc-900 dark:text-white group-hover:text-gold-600 dark:group-hover:text-gold-400 transition-colors leading-snug">
                                "Como a Mídia Manipula Estatísticas de Criminalidade"
                            </h4>
                            <p class="text-[11px] md:text-xs text-zinc-600 dark:text-zinc-400 font-light mt-2 line-clamp-2">
                                Higienização terminológica usada para anestesiar a opinião pública.
                            </p>
                        </div>
                        <div class="flex-shrink-0">
                            <img src="assets/monique_liberada.png" alt="Miniatura" class="w-16 h-16 md:w-20 md:h-20 object-cover rounded-lg group-hover:scale-105 transition-all duration-300" loading="lazy">
                        </div>
                    </a>

                    <!-- Item 6 -->
                    <a href="#" class="flex items-center justify-between p-4 bg-white/60 dark:bg-white/5 border border-zinc-200 dark:border-white/10 backdrop-blur-md rounded-xl hover:-translate-y-1 hover:shadow-lg hover:border-gold-500/30 transition-all duration-300 group" x-show="searchQuery === '' || $el.textContent.toLowerCase().includes(searchQuery.toLowerCase())">
                        <div class="pr-4 flex-grow">
                            <h4 class="font-playfair text-sm md:text-base font-bold text-zinc-900 dark:text-white group-hover:text-gold-600 dark:group-hover:text-gold-400 transition-colors leading-snug">
                                "O Ativismo Judicial como Ferramenta de Poder"
                            </h4>
                            <p class="text-[11px] md:text-xs text-zinc-600 dark:text-zinc-400 font-light mt-2 line-clamp-2">
                                Quando a toga substitui o voto na arquitetura estatal.
                            </p>
                        </div>
                        <div class="flex-shrink-0">
                            <img src="assets/messias_marcha.png" alt="Miniatura" class="w-16 h-16 md:w-20 md:h-20 object-cover rounded-lg group-hover:scale-105 transition-all duration-300" loading="lazy">
                        </div>
                    </a>

                </div>
            </section>

"""

if insertion_marker in content and 'id="mais-artigos"' not in content:
    new_content = content.replace(insertion_marker, new_section + insertion_marker)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Section inserted successfully.")
else:
    print("Insertion marker not found or section already exists.")

