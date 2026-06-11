import re

card_html = """
                    <!-- Card 6 -->
                    <div class="bg-white/60 dark:bg-white/5 border border-zinc-200 dark:border-white/10 backdrop-blur-md rounded-2xl overflow-hidden hover:-translate-y-2 hover:shadow-2xl hover:shadow-gold-500/5 hover:border-gold-500/30 transition-all duration-300 flex flex-col justify-between min-h-[440px] group">
                        
                        <!-- Container da Miniatura (Thumbnail) -->
                        <div class="relative w-full h-48 overflow-hidden bg-zinc-900 border-b border-zinc-200 dark:border-white/5">
                            <img src="assets/homeschooling_condenacao.png" alt="Miniatura Criminalização Homeschooling" class="w-full h-full object-cover transition-all duration-500 group-hover:scale-105 brightness-[1.1] contrast-[1.02] md:brightness-100 md:contrast-100" loading="lazy" decoding="async">
                        </div>

                        <!-- Corpo do Card -->
                        <div class="p-6 flex-grow flex flex-col justify-between space-y-4">
                            <div class="space-y-3">
                                <!-- Tag superior -->
                                <div class="flex items-center justify-between">
                                    <div class="inline-flex items-center space-x-1.5 px-2 py-0.5 bg-zinc-1550/60 dark:bg-white/5 border border-zinc-200 dark:border-white/10 rounded-md text-[9px] font-mono font-medium text-zinc-600 dark:text-zinc-300 uppercase tracking-wider">
                                        <span class="h-1.5 w-1.5 rounded-full bg-red-500 animate-pulse"></span>
                                        <span>INTERCEPTADO | G1 SP</span>
                                    </div>
                                    <span class="text-[9px] text-zinc-500 font-mono">28 de Abril, 2026</span>
                                </div>

                                <!-- Manchete -->
                                <h3 class="font-playfair text-base sm:text-lg font-bold text-zinc-900 dark:text-white group-hover:text-gold-600 dark:group-hover:text-gold-400 transition-colors leading-snug">
                                    "Pais são condenados por deixarem de levar filhas à escola no interior de SP"
                                </h3>

                                <!-- Resumo tático -->
                                <p class="text-xs text-zinc-600 dark:text-zinc-400 font-light leading-relaxed">
                                    A criminalização do ensino domiciliar através da Engenharia Social Coercitiva para forçar a doutrinação estatal.
                                </p>
                            </div>

                            <!-- Ação -->
                            <div class="pt-4 border-t border-zinc-200 dark:border-white/5">
                                <a href="analise-g1-homeschooling" class="inline-flex items-center text-xs font-semibold tracking-wider text-zinc-700 hover:text-gold-600 dark:text-zinc-300 dark:hover:text-gold-400 transition-colors uppercase">
                                    Iniciar Autópsia &nbsp;➔
                                </a>
                            </div>
                        </div>

                    </div>
"""

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Locate the end of Card 5 and insert Card 6
target = '<!-- Ação -->\\n                            <div class="pt-4 border-t border-zinc-200 dark:border-white/5">\\n                                <a href="analise-oglobo-messias" class="inline-flex items-center text-xs font-semibold tracking-wider text-zinc-700 hover:text-gold-600 dark:text-zinc-300 dark:hover:text-gold-400 transition-colors uppercase">\\n                                    Iniciar Autópsia &nbsp;➔\\n                                </a>\\n                            </div>\\n                        </div>\\n\\n                    </div>'

if target in content:
    content = content.replace(target, target + "\\n" + card_html)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Added Card 6 to index.html successfully.")
else:
    print("Could not find the insertion point.")
