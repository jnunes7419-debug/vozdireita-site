import re

def main():
    file_path = 'd:\\direita_intelectual\\index.html'
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    start_pattern = r'<div id="radar-grid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">\s*'
    end_pattern = r'\s*</div>\s*</section>\s*<!-- SEÇÃO MAIS ARTIGOS \(MINIATURAS\) -->'

    match_start = re.search(start_pattern, content)
    match_end = re.search(end_pattern, content)
    
    if not match_start or not match_end:
        print("Could not find radar grid.")
        return

    # EXACT RESTORE OF THE 6 CARDS
    card1 = """<!-- Card 1 -->
                    <div class="md:col-span-2 lg:col-span-2 bg-white/60 dark:bg-white/5 border border-zinc-200 dark:border-white/10 backdrop-blur-md rounded-2xl overflow-hidden hover:-translate-y-2 hover:shadow-2xl hover:shadow-gold-500/5 hover:border-gold-500/30 transition-all duration-300 flex flex-col justify-between min-h-[440px] group" x-transition >
                        <div class="relative w-full h-64 md:h-[22rem] overflow-hidden bg-zinc-900 border-b border-zinc-200 dark:border-white/5">
                            <img src="assets/geopolitica_israel_ira.png" alt="Miniatura Conflito Israel Irã" class="w-full h-full object-cover transition-all duration-500 group-hover:scale-105 brightness-[1.1] contrast-[1.02] md:brightness-100 md:contrast-100" loading="lazy" decoding="async">
                        </div>
                        <div class="p-6 flex-grow flex flex-col justify-between space-y-4">
                            <div class="space-y-3">
                                <div class="flex items-center justify-between">
                                    <div class="inline-flex items-center space-x-1.5 px-2 py-0.5 bg-zinc-1550/60 dark:bg-white/5 border border-zinc-200 dark:border-white/10 rounded-md text-[9px] font-mono font-medium text-zinc-600 dark:text-zinc-300 uppercase tracking-wider">
                                        <span class="h-1.5 w-1.5 rounded-full bg-red-500 animate-pulse"></span>
                                        <span>INTERCEPTADO | G1 MUNDO</span>
                                    </div>
                                    <span class="text-[9px] text-zinc-500 font-mono">07 de Junho, 2026</span>
                                </div>
                                <h3 class="font-playfair text-base sm:text-lg font-bold text-zinc-900 dark:text-white group-hover:text-gold-600 dark:group-hover:text-gold-400 transition-colors leading-snug">
                                    "Após bombardeios de Israel a Beirute, Irã lança mísseis..."
                                </h3>
                                <p class="text-xs text-zinc-600 dark:text-zinc-400 font-light leading-relaxed">
                                    Como a mídia inverte a agressão primária e omite o financiamento do terrorismo para proteger o eixo anti-Ocidente.
                                </p>
                            </div>
                            <div class="pt-4 border-t border-zinc-200 dark:border-white/5">
                                <a href="analise-geopolitica-israel-ira.html" class="inline-flex items-center text-xs font-semibold tracking-wider text-zinc-700 hover:text-gold-600 dark:text-zinc-300 dark:hover:text-gold-400 transition-colors uppercase">
                                    Iniciar Autópsia &nbsp;➔
                                </a>
                            </div>
                        </div>
                    </div>"""

    card2 = """<!-- Card 2 -->
                    <div class="bg-white/60 dark:bg-white/5 border border-zinc-200 dark:border-white/10 backdrop-blur-md rounded-2xl overflow-hidden hover:-translate-y-2 hover:shadow-2xl hover:shadow-gold-500/5 hover:border-gold-500/30 transition-all duration-300 flex flex-col justify-between min-h-[440px] group" x-transition >
                        <div class="relative w-full h-48 overflow-hidden bg-zinc-900 border-b border-zinc-200 dark:border-white/5">
                            <img src="assets/geopolitica_israel_ira.png" alt="Miniatura Conflito Israel Irã" class="w-full h-full object-cover transition-all duration-500 group-hover:scale-105 brightness-[1.1] contrast-[1.02] md:brightness-100 md:contrast-100" loading="lazy" decoding="async">
                        </div>
                        <div class="p-6 flex-grow flex flex-col justify-between space-y-4">
                            <div class="space-y-3">
                                <div class="flex items-center justify-between">
                                    <div class="inline-flex items-center space-x-1.5 px-2 py-0.5 bg-zinc-1550/60 dark:bg-white/5 border border-zinc-200 dark:border-white/10 rounded-md text-[9px] font-mono font-medium text-zinc-600 dark:text-zinc-300 uppercase tracking-wider">
                                        <span class="h-1.5 w-1.5 rounded-full bg-red-500 animate-pulse"></span>
                                        <span>INTERCEPTADO | G1 MUNDO</span>
                                    </div>
                                    <span class="text-[9px] text-zinc-500 font-mono">07 de Junho, 2026</span>
                                </div>
                                <h3 class="font-playfair text-base sm:text-lg font-bold text-zinc-900 dark:text-white group-hover:text-gold-600 dark:group-hover:text-gold-400 transition-colors leading-snug">
                                    "Após bombardeios de Israel a Beirute, Irã lança mísseis..."
                                </h3>
                                <p class="text-xs text-zinc-600 dark:text-zinc-400 font-light leading-relaxed">
                                    Como a mídia inverte a agressão primária e omite o financiamento do terrorismo para proteger o eixo anti-Ocidente.
                                </p>
                            </div>
                            <div class="pt-4 border-t border-zinc-200 dark:border-white/5">
                                <a href="analise-geopolitica-israel-ira.html" class="inline-flex items-center text-xs font-semibold tracking-wider text-zinc-700 hover:text-gold-600 dark:text-zinc-300 dark:hover:text-gold-400 transition-colors uppercase">
                                    Iniciar Autópsia &nbsp;➔
                                </a>
                            </div>
                        </div>
                    </div>"""

    card3 = """<!-- Card 3 -->
                    <div class="bg-white/60 dark:bg-white/5 border border-zinc-200 dark:border-white/10 backdrop-blur-md rounded-2xl overflow-hidden hover:-translate-y-2 hover:shadow-2xl hover:shadow-gold-500/5 hover:border-gold-500/30 transition-all duration-300 flex flex-col justify-between min-h-[440px] group" x-transition >
                        <div class="relative w-full h-48 overflow-hidden bg-zinc-900 border-b border-zinc-200 dark:border-white/5">
                            <img src="assets/homeschooling_condenacao.png" alt="Miniatura Criminalização Homeschooling" class="w-full h-full object-cover transition-all duration-500 group-hover:scale-105 brightness-[1.1] contrast-[1.02] md:brightness-100 md:contrast-100" loading="lazy" decoding="async">
                        </div>
                        <div class="p-6 flex-grow flex flex-col justify-between space-y-4">
                            <div class="space-y-3">
                                <div class="flex items-center justify-between">
                                    <div class="inline-flex items-center space-x-1.5 px-2 py-0.5 bg-zinc-1550/60 dark:bg-white/5 border border-zinc-200 dark:border-white/10 rounded-md text-[9px] font-mono font-medium text-zinc-600 dark:text-zinc-300 uppercase tracking-wider">
                                        <span class="h-1.5 w-1.5 rounded-full bg-red-500 animate-pulse"></span>
                                        <span>INTERCEPTADO | G1</span>
                                    </div>
                                    <span class="text-[9px] text-zinc-500 font-mono">07 de Junho, 2026</span>
                                </div>
                                <h3 class="font-playfair text-base sm:text-lg font-bold text-zinc-900 dark:text-white group-hover:text-gold-600 dark:group-hover:text-gold-400 transition-colors leading-snug">
                                    "Pais são condenados por não levarem filhas à escola..."
                                </h3>
                                <p class="text-xs text-zinc-600 dark:text-zinc-400 font-light leading-relaxed">
                                    A criminalização do ensino domiciliar através da Engenharia Social Coercitiva e a hipertrofia do Estado.
                                </p>
                            </div>
                            <div class="pt-4 border-t border-zinc-200 dark:border-white/5">
                                <a href="analise-g1-homeschooling.html" class="inline-flex items-center text-xs font-semibold tracking-wider text-zinc-700 hover:text-gold-600 dark:text-zinc-300 dark:hover:text-gold-400 transition-colors uppercase">
                                    Iniciar Autópsia &nbsp;➔
                                </a>
                            </div>
                        </div>
                    </div>"""

    card4 = """<!-- Card 4 -->
                    <div class="bg-white/60 dark:bg-white/5 border border-zinc-200 dark:border-white/10 backdrop-blur-md rounded-2xl overflow-hidden hover:-translate-y-2 hover:shadow-2xl hover:shadow-gold-500/5 hover:border-gold-500/30 transition-all duration-300 flex flex-col justify-between min-h-[440px] group" x-transition >
                        <div class="relative w-full h-48 overflow-hidden bg-zinc-900 border-b border-zinc-200 dark:border-white/5">
                            <img src="assets/tornozeleira_rosa.png" alt="Miniatura Fetiche da Tornozeleira Rosa" class="w-full h-full object-cover transition-all duration-500 group-hover:scale-105 brightness-[1.1] contrast-[1.02] md:brightness-100 md:contrast-100" loading="lazy" decoding="async">
                        </div>
                        <div class="p-6 flex-grow flex flex-col justify-between space-y-4">
                            <div class="space-y-3">
                                <div class="flex items-center justify-between">
                                    <div class="inline-flex items-center space-x-1.5 px-2 py-0.5 bg-zinc-1550/60 dark:bg-white/5 border border-zinc-200 dark:border-white/10 rounded-md text-[9px] font-mono font-medium text-zinc-600 dark:text-zinc-300 uppercase tracking-wider">
                                        <span class="h-1.5 w-1.5 rounded-full bg-red-500 animate-pulse"></span>
                                        <span>INTERCEPTADO | O GLOBO</span>
                                    </div>
                                    <span class="text-[9px] text-zinc-500 font-mono">07 de Junho, 2026</span>
                                </div>
                                <h3 class="font-playfair text-base sm:text-lg font-bold text-zinc-900 dark:text-white group-hover:text-gold-600 dark:group-hover:text-gold-400 transition-colors leading-snug">
                                    "A Armadilha do Cavalo de Troia no PL 1811/2026"
                                </h3>
                                <p class="text-xs text-zinc-600 dark:text-zinc-400 font-light leading-relaxed">
                                    Como a tornozeleira rosa atua como um Cavalo de Troia ideológico para cindir a base conservadora em ano eleitoral e impor o punitivismo de gênero.
                                </p>
                            </div>
                            <div class="pt-4 border-t border-zinc-200 dark:border-white/5">
                                <a href="analise-oglobo-rosa.html" class="inline-flex items-center text-xs font-semibold tracking-wider text-zinc-700 hover:text-gold-600 dark:text-zinc-300 dark:hover:text-gold-400 transition-colors uppercase">
                                    Iniciar Autópsia &nbsp;➔
                                </a>
                            </div>
                        </div>
                    </div>"""

    card5 = """<!-- Card 5 -->
                    <div class="bg-white/60 dark:bg-white/5 border border-zinc-200 dark:border-white/10 backdrop-blur-md rounded-2xl overflow-hidden hover:-translate-y-2 hover:shadow-2xl hover:shadow-gold-500/5 hover:border-gold-500/30 transition-all duration-300 flex flex-col justify-between min-h-[440px] group" x-transition >
                        <div class="relative w-full h-48 overflow-hidden bg-zinc-900 border-b border-zinc-200 dark:border-white/5">
                            <img src="assets/monique_liberada.png" alt="Miniatura A Simetria do Privilégio" class="w-full h-full object-cover transition-all duration-500 group-hover:scale-105 brightness-[1.1] contrast-[1.02] md:brightness-100 md:contrast-100" loading="lazy" decoding="async">
                        </div>
                        <div class="p-6 flex-grow flex flex-col justify-between space-y-4">
                            <div class="space-y-3">
                                <div class="flex items-center justify-between">
                                    <div class="inline-flex items-center space-x-1.5 px-2 py-0.5 bg-zinc-1550/60 dark:bg-white/5 border border-zinc-200 dark:border-white/10 rounded-md text-[9px] font-mono font-medium text-zinc-600 dark:text-zinc-300 uppercase tracking-wider">
                                        <span class="h-1.5 w-1.5 rounded-full bg-red-500 animate-pulse"></span>
                                        <span>INTERCEPTADO | G1 GLOBO</span>
                                    </div>
                                    <span class="text-[9px] text-zinc-500 font-mono">07 de Junho, 2026</span>
                                </div>
                                <h3 class="font-playfair text-base sm:text-lg font-bold text-zinc-900 dark:text-white group-hover:text-gold-600 dark:group-hover:text-gold-400 transition-colors leading-snug">
                                    "Decisão libera Monique Medeiros da prisão preventiva"
                                </h3>
                                <p class="text-xs text-zinc-600 dark:text-zinc-400 font-light leading-relaxed">
                                    Como o progressismo autoritário e a engenharia social coercitiva atuam para desarmar a severidade penal e anestesiar a opinião pública.
                                </p>
                            </div>
                            <div class="pt-4 border-t border-zinc-200 dark:border-white/5">
                                <a href="analise-g1-monique.html" class="inline-flex items-center text-xs font-semibold tracking-wider text-zinc-700 hover:text-gold-600 dark:text-zinc-300 dark:hover:text-gold-400 transition-colors uppercase">
                                    Iniciar Autópsia &nbsp;➔
                                </a>
                            </div>
                        </div>
                    </div>"""

    card6 = """<!-- Card 6 -->
                    <div class="hidden md:flex bg-white/60 dark:bg-white/5 border border-zinc-200 dark:border-white/10 backdrop-blur-md rounded-2xl overflow-hidden hover:-translate-y-2 hover:shadow-2xl hover:shadow-gold-500/5 hover:border-gold-500/30 transition-all duration-300 flex flex-col justify-between min-h-[440px] group" x-transition >
                        <div class="relative w-full h-48 overflow-hidden bg-zinc-900 border-b border-zinc-200 dark:border-white/5">
                            <img src="assets/seguranca_rj.png" alt="Miniatura Feitiço do Terrorismo" class="w-full h-full object-cover transition-all duration-500 group-hover:scale-105 brightness-[1.1] contrast-[1.02] md:brightness-100 md:contrast-100" loading="lazy" decoding="async">
                        </div>
                        <div class="p-6 flex-grow flex flex-col justify-between space-y-4">
                            <div class="space-y-3">
                                <div class="flex items-center justify-between">
                                    <div class="inline-flex items-center space-x-1.5 px-2 py-0.5 bg-zinc-1550/60 dark:bg-white/5 border border-zinc-200 dark:border-white/10 rounded-md text-[9px] font-mono font-medium text-zinc-600 dark:text-zinc-300 uppercase tracking-wider">
                                        <span class="h-1.5 w-1.5 rounded-full bg-amber-500 animate-pulse"></span>
                                        <span>INTERCEPTADO | UOL</span>
                                    </div>
                                    <span class="text-[9px] text-zinc-500 font-mono">06 de Junho, 2026</span>
                                </div>
                                <h3 class="font-playfair text-base sm:text-lg font-bold text-zinc-900 dark:text-white group-hover:text-gold-600 dark:group-hover:text-gold-400 transition-colors leading-snug">
                                    "Feitiço do terrorismo pode enfeitiçar Flávio Bolsonaro"
                                </h3>
                                <p class="text-xs text-zinc-600 dark:text-zinc-400 font-light leading-relaxed">
                                    Como a esquerda neototalitária tenta criminalizar a oposição e blindar facções criminosas usando malabarismo associativo.
                                </p>
                            </div>
                            <div class="pt-4 border-t border-zinc-200 dark:border-white/5">
                                <a href="analise-uol-terrorismo.html" class="inline-flex items-center text-xs font-semibold tracking-wider text-zinc-700 hover:text-gold-600 dark:text-zinc-300 dark:hover:text-gold-400 transition-colors uppercase">
                                    Iniciar Autópsia &nbsp;➔
                                </a>
                            </div>
                        </div>
                    </div>"""

    new_grid_content = "\n\n".join([card1, card2, card3, card4, card5, card6]) + "\n\n"

    new_content = content[:match_start.end()] + new_grid_content + content[match_end.start():]

    # Note: we MUST NOT revert the cookies notice position because the user explicitly said:
    # "outro ponto também... o botão de subir... tenta fazer isso aí". 
    # He wants the cookie notice change to stay, but the structure of cards to revert!

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print("Grid reverted to the exact praised state!")

if __name__ == '__main__':
    main()
