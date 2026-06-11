import re

def main():
    file_path = 'd:\\direita_intelectual\\index.html'
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # We will redefine all 6 cards exactly
    cards = [
        # Card 1: CartaCapital Pesquisa ES
        """
                    <div class="md:col-span-2 lg:col-span-2 bg-white/60 dark:bg-white/5 border border-zinc-200 dark:border-white/10 backdrop-blur-md rounded-2xl overflow-hidden hover:-translate-y-2 hover:shadow-2xl hover:shadow-gold-500/5 hover:border-gold-500/30 transition-all duration-300 flex flex-col justify-between min-h-[440px] group" x-transition >
                        <div class="relative w-full h-64 md:h-[22rem] overflow-hidden bg-zinc-900 border-b border-zinc-200 dark:border-white/5">
                            <img src="assets/grafico_pesquisa_es_1781048521496.png" alt="Miniatura Pesquisa Espírito Santo" class="w-full h-full object-cover transition-all duration-500 group-hover:scale-105 brightness-[1.1] contrast-[1.02] md:brightness-100 md:contrast-100" loading="lazy" decoding="async">
                        </div>
                        <div class="p-6 flex-grow flex flex-col justify-between space-y-4">
                            <div class="space-y-3">
                                <div class="flex items-center justify-between">
                                    <div class="inline-flex items-center space-x-1.5 px-2 py-0.5 bg-zinc-1550/60 dark:bg-white/5 border border-zinc-200 dark:border-white/10 rounded-md text-[9px] font-mono font-medium text-zinc-600 dark:text-zinc-300 uppercase tracking-wider">
                                        <span class="h-1.5 w-1.5 rounded-full bg-red-500 animate-pulse"></span>
                                        <span>INTERCEPTADO | CARTA CAPITAL</span>
                                    </div>
                                    <span class="text-[9px] text-zinc-500 font-mono">09 de Junho, 2026</span>
                                </div>
                                <h3 class="font-playfair text-base sm:text-lg font-bold text-zinc-900 dark:text-white group-hover:text-gold-600 dark:group-hover:text-gold-400 transition-colors leading-snug">
                                    "A disputa entre Lula e Flávio Bolsonaro no Espírito Santo..."
                                </h3>
                                <p class="text-xs text-zinc-600 dark:text-zinc-400 font-light leading-relaxed">
                                    Como a mídia utiliza a manobra de "supressão de horizonte" para esconder a derrota do governo no 2º turno.
                                </p>
                            </div>
                            <div class="pt-4 border-t border-zinc-200 dark:border-white/5">
                                <a href="analise-carta-capital-pesquisa.html" class="inline-flex items-center text-xs font-semibold tracking-wider text-zinc-700 hover:text-gold-600 dark:text-zinc-300 dark:hover:text-gold-400 transition-colors uppercase">
                                    Iniciar Autópsia &nbsp;➔
                                </a>
                            </div>
                        </div>
                    </div>
        """,
        # Card 2: Ypê
        """
                    <div class="bg-white/60 dark:bg-white/5 border border-zinc-200 dark:border-white/10 backdrop-blur-md rounded-2xl overflow-hidden hover:-translate-y-2 hover:shadow-2xl hover:shadow-gold-500/5 hover:border-gold-500/30 transition-all duration-300 flex flex-col justify-between min-h-[440px] group" x-transition >
                        <div class="relative w-full h-48 overflow-hidden bg-zinc-900 border-b border-zinc-200 dark:border-white/5">
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
                                    "Ypê: final 1 no lote identifica produtos..."
                                </h3>
                                <p class="text-xs text-zinc-600 dark:text-zinc-400 font-light leading-relaxed">
                                    A esquerda neototalitária usa a Anvisa para retaliar a Ypê pela doação de R$ 1,5 milhão a Bolsonaro.
                                </p>
                            </div>
                            <div class="pt-4 border-t border-zinc-200 dark:border-white/5">
                                <a href="analise-g1-ype.html" class="inline-flex items-center text-xs font-semibold tracking-wider text-zinc-700 hover:text-gold-600 dark:text-zinc-300 dark:hover:text-gold-400 transition-colors uppercase">
                                    Iniciar Autópsia &nbsp;➔
                                </a>
                            </div>
                        </div>
                    </div>
        """,
        # Card 3: Geopolítica
        """
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
                                    "Após bombardeios de Israel a Beirute..."
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
                    </div>
        """,
        # Card 4: Homeschooling
        """
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
                                    "Pais são condenados por não levarem filhas..."
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
                    </div>
        """,
        # Card 5: Tornozeleira Rosa
        """
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
                    </div>
        """,
        # Card 6: Monique Medeiros
        """
                    <div class="bg-white/60 dark:bg-white/5 border border-zinc-200 dark:border-white/10 backdrop-blur-md rounded-2xl overflow-hidden hover:-translate-y-2 hover:shadow-2xl hover:shadow-gold-500/5 hover:border-gold-500/30 transition-all duration-300 flex flex-col justify-between min-h-[440px] group" x-transition >
                        <div class="relative w-full h-48 overflow-hidden bg-zinc-900 border-b border-zinc-200 dark:border-white/5">
                            <img src="assets/monique_liberada.png" alt="Miniatura Monique Medeiros" class="w-full h-full object-cover transition-all duration-500 group-hover:scale-105 brightness-[1.1] contrast-[1.02] md:brightness-100 md:contrast-100" loading="lazy" decoding="async">
                        </div>
                        <div class="p-6 flex-grow flex flex-col justify-between space-y-4">
                            <div class="space-y-3">
                                <div class="flex items-center justify-between">
                                    <div class="inline-flex items-center space-x-1.5 px-2 py-0.5 bg-zinc-1550/60 dark:bg-white/5 border border-zinc-200 dark:border-white/10 rounded-md text-[9px] font-mono font-medium text-zinc-600 dark:text-zinc-300 uppercase tracking-wider">
                                        <span class="h-1.5 w-1.5 rounded-full bg-red-500 animate-pulse"></span>
                                        <span>INTERCEPTADO | G1</span>
                                    </div>
                                    <span class="text-[9px] text-zinc-500 font-mono">03 de Junho, 2026</span>
                                </div>
                                <h3 class="font-playfair text-base sm:text-lg font-bold text-zinc-900 dark:text-white group-hover:text-gold-600 dark:group-hover:text-gold-400 transition-colors leading-snug">
                                    "Decisão libera Monique Medeiros da prisão"
                                </h3>
                                <p class="text-xs text-zinc-600 dark:text-zinc-400 font-light leading-relaxed">
                                    O progressismo autoritário e a anestesia da opinião pública frente à seletividade penal.
                                </p>
                            </div>
                            <div class="pt-4 border-t border-zinc-200 dark:border-white/5">
                                <a href="analise-g1-monique.html" class="inline-flex items-center text-xs font-semibold tracking-wider text-zinc-700 hover:text-gold-600 dark:text-zinc-300 dark:hover:text-gold-400 transition-colors uppercase">
                                    Iniciar Autópsia &nbsp;➔
                                </a>
                            </div>
                        </div>
                    </div>
        """
    ]

    start_pattern = r'<div id="radar-grid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">\s*'
    end_pattern = r'\s*</div>\s*</section>\s*<!-- SEÇÃO MAIS ARTIGOS \(MINIATURAS\) -->'

    match_start = re.search(start_pattern, content)
    match_end = re.search(end_pattern, content)

    if not match_start or not match_end:
        print("Could not find radar grid.")
        return

    new_grid_content = ""
    for i, c in enumerate(cards):
        new_grid_content += f"<!-- Card {i+1} -->\n{c.strip()}\n\n"

    new_content = content[:match_start.end()] + new_grid_content + content[match_end.start():]

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print("Cards rebuilt successfully!")

if __name__ == '__main__':
    main()
