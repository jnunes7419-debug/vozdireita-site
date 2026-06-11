import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Locate the start and end of the Grid de Pôsteres
start_marker = "<!-- Grid de Pôsteres (Aspect 2/3 com Glassmorphism) -->"
end_marker = "</section>\n\n            <!-- SEÇÃO 3: A HEGEMONIA DO JORNALISMO -->"

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx != -1 and end_idx != -1:
    old_grid = content[start_idx:end_idx]
    
    new_grid = """<!-- Grid de Cards Menores e Mais Clean -->
                <div class="grid grid-cols-1 md:grid-cols-3 gap-6">

                    <!-- Card 1 -->
                    <a href="dossie-doutrinacao"
                        class="group flex flex-col bg-white/80 dark:bg-zinc-900/40 border border-zinc-200 dark:border-white/10 rounded-2xl overflow-hidden hover:shadow-xl hover:border-gold-500/30 transition-all duration-300 backdrop-blur-md">
                        <!-- Miniatura (16:9) -->
                        <div class="relative aspect-video overflow-hidden bg-zinc-100 dark:bg-zinc-950">
                            <img src="assets/guerra_pop_1.png" alt="Doutrinação Invisível"
                                class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" loading="lazy" decoding="async">
                        </div>
                        <!-- Informações Clean -->
                        <div class="p-6 flex flex-col flex-grow">
                            <span class="text-[10px] font-bold tracking-widest text-gold-600 dark:text-gold-500 uppercase mb-2">DOCUMENTÁRIO • 2026</span>
                            <h3 class="font-playfair text-xl font-bold text-zinc-900 dark:text-white mb-2 leading-tight group-hover:text-gold-600 dark:group-hover:text-gold-400 transition-colors">
                                Doutrinação Invisível
                            </h3>
                            <p class="text-zinc-600 dark:text-zinc-400 text-xs font-light leading-relaxed flex-grow">
                                Como produções de massas moldam o inconsciente coletivo ao redefinir a moral familiar e as virtudes tradicionais de forma velada.
                            </p>
                            <div class="mt-5 flex items-center space-x-2 text-[10px] font-bold text-zinc-400 dark:text-zinc-500 uppercase tracking-widest group-hover:text-gold-600 dark:group-hover:text-gold-500 transition-colors">
                                <span>Acessar Análise</span>
                                <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3" viewBox="0 0 20 20" fill="currentColor">
                                    <path fill-rule="evenodd" d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z" clip-rule="evenodd" />
                                </svg>
                            </div>
                        </div>
                    </a>

                    <!-- Card 2 -->
                    <a href="dossie-valores"
                        class="group flex flex-col bg-white/80 dark:bg-zinc-900/40 border border-zinc-200 dark:border-white/10 rounded-2xl overflow-hidden hover:shadow-xl hover:border-gold-500/30 transition-all duration-300 backdrop-blur-md">
                        <div class="relative aspect-video overflow-hidden bg-zinc-100 dark:bg-zinc-950">
                            <img src="assets/guerra_pop_2.png" alt="Subversão de Valores"
                                class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" loading="lazy" decoding="async">
                        </div>
                        <div class="p-6 flex flex-col flex-grow">
                            <span class="text-[10px] font-bold tracking-widest text-gold-600 dark:text-gold-500 uppercase mb-2">SÉRIE ESPECIAL • 2026</span>
                            <h3 class="font-playfair text-xl font-bold text-zinc-900 dark:text-white mb-2 leading-tight group-hover:text-gold-600 dark:group-hover:text-gold-400 transition-colors">
                                Subversão de Valores
                            </h3>
                            <p class="text-zinc-600 dark:text-zinc-400 text-xs font-light leading-relaxed flex-grow">
                                A desconstrução sistemática de figuras heroicas clássicas e a normalização de protagonistas amorais nas narrativas modernas.
                            </p>
                            <div class="mt-5 flex items-center space-x-2 text-[10px] font-bold text-zinc-400 dark:text-zinc-500 uppercase tracking-widest group-hover:text-gold-600 dark:group-hover:text-gold-500 transition-colors">
                                <span>Acessar Análise</span>
                                <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3" viewBox="0 0 20 20" fill="currentColor">
                                    <path fill-rule="evenodd" d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z" clip-rule="evenodd" />
                                </svg>
                            </div>
                        </div>
                    </a>

                    <!-- Card 3 -->
                    <a href="dossie-silicio"
                        class="group flex flex-col bg-white/80 dark:bg-zinc-900/40 border border-zinc-200 dark:border-white/10 rounded-2xl overflow-hidden hover:shadow-xl hover:border-gold-500/30 transition-all duration-300 backdrop-blur-md">
                        <div class="relative aspect-video overflow-hidden bg-zinc-100 dark:bg-zinc-950">
                            <img src="assets/chess_strategy_bg.png" alt="Telas de Silício"
                                class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" loading="lazy" decoding="async">
                        </div>
                        <div class="p-6 flex flex-col flex-grow">
                            <span class="text-[10px] font-bold tracking-widest text-gold-600 dark:text-gold-500 uppercase mb-2">INVESTIGAÇÃO • 2026</span>
                            <h3 class="font-playfair text-xl font-bold text-zinc-900 dark:text-white mb-2 leading-tight group-hover:text-gold-600 dark:group-hover:text-gold-400 transition-colors">
                                Telas de Silício
                            </h3>
                            <p class="text-zinc-600 dark:text-zinc-400 text-xs font-light leading-relaxed flex-grow">
                                O papel dos algoritmos de recomendação na indução de comportamentos e filtragem de visões de mundo conservadoras.
                            </p>
                            <div class="mt-5 flex items-center space-x-2 text-[10px] font-bold text-zinc-400 dark:text-zinc-500 uppercase tracking-widest group-hover:text-gold-600 dark:group-hover:text-gold-500 transition-colors">
                                <span>Acessar Análise</span>
                                <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3" viewBox="0 0 20 20" fill="currentColor">
                                    <path fill-rule="evenodd" d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z" clip-rule="evenodd" />
                                </svg>
                            </div>
                        </div>
                    </a>

                </div>
            """
    content = content.replace(old_grid, new_grid)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Cards redesign applied successfully.")
else:
    print("Could not find the target section.")
