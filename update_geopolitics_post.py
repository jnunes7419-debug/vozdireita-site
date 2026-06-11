import os

def update_modelo_post():
    with open('analise-oglobo-rosa.html', 'r', encoding='utf-8') as f:
        analise = f.read()
    
    header_end = analise.find('</header>') + len('</header>')
    head_header = analise[:header_end]
    
    footer_start_idx = analise.find('<!-- FOOTER (RODAPÉ) -->')
    footer = analise[footer_start_idx:]
    
    main_content = """

    <!-- HERO EDITORIAL PREMIUM -->
    <section class="relative w-full h-[85vh] min-h-[600px] flex items-end justify-center overflow-hidden bg-black">
        <!-- Imagem de Fundo Completa com Efeito Parallax Simulado -->
        <div class="absolute inset-0 w-full h-full">
            <img src="assets/geopolitica_israel_ira.png" alt="Imagem de Destaque - Israel e Irã" class="w-full h-full object-cover opacity-60 dark:opacity-40 transform scale-105 transition-transform duration-[10s] hover:scale-100">
            <!-- Overlay de Gradiente Escuro para Leitura -->
            <div class="absolute inset-0 bg-gradient-to-t from-black via-black/60 to-transparent"></div>
            <div class="absolute inset-0 bg-gradient-to-r from-black/80 via-transparent to-transparent"></div>
        </div>

        <!-- Conteúdo do Hero -->
        <div class="relative z-10 max-w-[1200px] w-full px-8 pb-16 md:pb-24">
            
            <!-- Tags e Metadados Acima do Título -->
            <div class="flex items-center space-x-4 mb-6">
                <span class="px-3 py-1 bg-gold-600/90 backdrop-blur-md text-white text-[10px] font-bold uppercase tracking-widest rounded-sm shadow-lg">Geopolítica Global</span>
                <span class="text-zinc-300 text-xs font-mono tracking-wider flex items-center">
                    <svg class="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                    Tempo de Leitura: 5 min
                </span>
            </div>

            <!-- Título Gigante e Impactante -->
            <h1 class="font-playfair text-5xl md:text-7xl lg:text-8xl font-bold tracking-tight text-white leading-[1.1] mb-6 drop-shadow-2xl max-w-4xl">
                A Inversão de Culpabilidade: O Eixo Irã-Israel
            </h1>
            
            <!-- Subtítulo / Gancho -->
            <h2 class="font-jakarta text-xl md:text-2xl text-zinc-300 font-light max-w-3xl leading-relaxed border-l-4 border-gold-500 pl-6 drop-shadow-lg">
                Como a Hegemonia do Jornalismo manipula a linha do tempo do conflito para transformar agressores contumazes em vítimas e nações soberanas em vilões.
            </h2>
            
        </div>
    </section>

    <!-- ÁREA DE CONTEÚDO PRINCIPAL -->
    <main class="relative z-20 flex-grow bg-slate-50 dark:bg-[#0a0a0a] transition-colors duration-300">
        
        <div class="max-w-[1400px] w-full px-4 sm:px-8 mx-auto py-16 md:py-24 grid grid-cols-1 lg:grid-cols-12 gap-16">
            
            <!-- SIDEBAR ESQUERDA (Autor e Compartilhamento) -->
            <aside class="hidden lg:block lg:col-span-3">
                <div class="sticky top-32 space-y-10">
                    
                    <!-- Perfil Premium do Autor -->
                    <div class="bg-white dark:bg-zinc-900/40 border border-zinc-200 dark:border-white/5 rounded-2xl p-6 text-center shadow-xl backdrop-blur-sm">
                        <div class="relative w-24 h-24 mx-auto mb-4">
                            <div class="absolute inset-0 bg-gold-500 rounded-full animate-pulse opacity-20"></div>
                            <img src="assets/jander_nunes_profile.png" alt="Jander Nunes" class="relative w-full h-full rounded-full object-cover border-2 border-gold-500/50 shadow-md">
                        </div>
                        <h3 class="font-playfair text-xl font-bold text-zinc-900 dark:text-white mb-1">Jander Nunes</h3>
                        <p class="text-xs font-mono uppercase tracking-widest text-gold-600 dark:text-gold-400 mb-4">Estrategista Chefe</p>
                        <p class="text-sm font-light text-zinc-600 dark:text-zinc-400 italic">"Desconstruindo a hegemonia cultural através da lógica implacável."</p>
                    </div>

                    <!-- Indicador de Progresso (Simulado) e Links -->
                    <div class="hidden xl:block">
                        <h4 class="text-xs font-bold uppercase tracking-widest text-zinc-400 mb-4 border-b border-zinc-200 dark:border-zinc-800 pb-2">Índice da Autópsia</h4>
                        <ul class="space-y-3 text-sm font-jakarta text-zinc-500 dark:text-zinc-400">
                            <li><a href="#artigo-inicio" class="hover:text-gold-500 transition-colors flex items-center"><span class="w-1.5 h-1.5 rounded-full bg-gold-500 mr-2"></span> A Manchete Original</a></li>
                            <li><a href="#realidade-oculta" class="hover:text-gold-500 transition-colors flex items-center"><span class="w-1.5 h-1.5 rounded-full bg-zinc-300 dark:bg-zinc-700 mr-2"></span> A Realidade Oculta</a></li>
                            <li><a href="#diagnostico" class="hover:text-gold-500 transition-colors flex items-center"><span class="w-1.5 h-1.5 rounded-full bg-zinc-300 dark:bg-zinc-700 mr-2"></span> A Ação Neototalitária</a></li>
                            <li><a href="#manual" class="hover:text-gold-500 transition-colors flex items-center"><span class="w-1.5 h-1.5 rounded-full bg-zinc-300 dark:bg-zinc-700 mr-2"></span> Arma Intelectual</a></li>
                        </ul>
                    </div>

                </div>
            </aside>

            <!-- COLUNA CENTRAL (O Artigo) -->
            <div class="lg:col-span-8 2xl:col-span-7 space-y-12">

                <!-- 1. A MANCHETE OFICIAL -->
                <article id="artigo-inicio" class="prose prose-zinc dark:prose-invert max-w-none text-lg md:text-xl leading-relaxed font-jakarta font-light text-zinc-800 dark:text-zinc-300 scroll-mt-24
                    prose-p:mb-8 prose-strong:text-zinc-900 dark:prose-strong:text-white prose-strong:font-semibold">
                    
                    <h3 class="font-playfair text-3xl font-bold text-zinc-900 dark:text-white mb-6 border-l-4 border-gold-500 pl-4">
                        1. A MANCHETE OFICIAL (A Isca)
                    </h3>
                    
                    <div class="p-6 bg-zinc-100 dark:bg-zinc-900/50 rounded-lg border border-zinc-200 dark:border-zinc-800 mb-8 italic">
                        "Após bombardeios de Israel a Beirute, Irã lança mísseis em direção ao território israelense; Netanyahu diz que haverá resposta"
                    </div>
                    
                    <p>
                        <strong>A Falsa Premissa:</strong> O texto inverte a cronologia moral do conflito, estruturando a manchete para apresentar o ataque iraniano como uma "reação justificável" e rotulando a autodefesa de Israel como a agressão primária.
                    </p>

                </article>

                <!-- 2. A AUTÓPSIA DO FATO -->
                <article id="realidade-oculta" class="prose prose-zinc dark:prose-invert max-w-none text-lg md:text-xl leading-relaxed font-jakarta font-light text-zinc-800 dark:text-zinc-300 scroll-mt-24
                    prose-p:mb-8 prose-strong:text-zinc-900 dark:prose-strong:text-white prose-strong:font-semibold mt-16">
                    
                    <h3 class="font-playfair text-3xl font-bold text-zinc-900 dark:text-white mb-6 border-l-4 border-gold-500 pl-4">
                        2. A AUTÓPSIA DO FATO (A Realidade Oculta)
                    </h3>
                    
                    <ul class="space-y-4 list-disc list-inside">
                        <li><strong>Omissão de Causalidade Contínua:</strong> A matéria trata o ataque israelense em Beirute de forma isolada, omitindo que o Hezbollah (proxy militar financiado pelo Irã) utiliza o Líbano como base para disparar foguetes diariamente contra civis no norte de Israel, forçando o esvaziamento de cidades inteiras.</li>
                        <li><strong>Falsa Equivalência Moral:</strong> A redação equipara as Forças de Defesa de Israel — que alvejam instalações e líderes terroristas baseados em inteligência prévia — à Guarda Revolucionária Iraniana, uma engrenagem de terrorismo de Estado que lança mísseis balísticos indiscriminadamente contra o território israelense.</li>
                        <li><strong>Isolamento de Liderança via Autoridade:</strong> O destaque para a suposta pressão do governo americano ("não tem escolha") serve ao propósito narrativo de pintar a liderança de Israel como um obstáculo insubordinado à paz, camuflando o fato de que acordos lenientes com Teerã apenas oxigenam o terrorismo na região.</li>
                    </ul>

                </article>

                <!-- Pull Quote Elegante -->
                <blockquote class="relative my-16 p-8 md:p-12 text-center bg-zinc-100/50 dark:bg-zinc-900/30 rounded-3xl border border-zinc-200/50 dark:border-white/5 shadow-inner">
                    <svg class="absolute top-4 left-6 w-12 h-12 text-gold-500/20" fill="currentColor" viewBox="0 0 24 24"><path d="M14.017 21v-7.391c0-5.704 3.731-9.57 8.983-10.609l.995 2.151c-2.432.917-3.995 3.638-3.995 5.849h4v10h-9.983zm-14.017 0v-7.391c0-5.704 3.748-9.57 9-10.609l.996 2.151c-2.433.917-3.996 3.638-3.996 5.849h3.983v10h-9.983z"/></svg>
                    <p class="font-playfair text-2xl md:text-3xl font-medium text-zinc-900 dark:text-gold-400 italic mb-0 leading-tight">
                        "Transformar o direito soberano de autodefesa em crime de guerra é o triunfo máximo da Engenharia Social na cobertura internacional."
                    </p>
                </blockquote>

                <!-- 3. O DIAGNÓSTICO DA TÁTICA -->
                <article id="diagnostico" class="prose prose-zinc dark:prose-invert max-w-none text-lg md:text-xl leading-relaxed font-jakarta font-light text-zinc-800 dark:text-zinc-300 scroll-mt-24
                    prose-p:mb-8 prose-strong:text-zinc-900 dark:prose-strong:text-white prose-strong:font-semibold">
                    
                    <h3 class="font-playfair text-3xl font-bold text-zinc-900 dark:text-white mb-6 border-l-4 border-gold-500 pl-4">
                        3. O DIAGNÓSTICO DA TÁTICA (A Ação Neototalitária)
                    </h3>
                    
                    <p>
                        A <strong>Esquerda Neototalitária</strong> aplica aqui a tática clássica de <strong>Inversão de Culpabilidade</strong>. Ao abrir a manchete com a condicional "Após bombardeios de Israel", a redação utiliza Engenharia Social Coercitiva para programar o leitor a isentar o eixo terrorista do Irã de responsabilidade, enquadrando-o falsamente na posição de legítima defesa.
                    </p>
                    <p>
                        O Progressismo Autoritário, infiltrado nas redações, protege regimes opressores ao esvaziar e criminalizar o direito soberano de defesa das democracias ocidentais, embalando essa desonestidade sob o verniz de "jornalismo isento".
                    </p>

                </article>

                <!-- 4. MANUAL DE DEFESA -->
                <div id="manual" class="mt-16 space-y-12 scroll-mt-24">
                    
                    <!-- Análise Box (Glassmorphism Escuro) -->
                    <div class="relative bg-zinc-900 dark:bg-black border border-zinc-800 dark:border-zinc-800/50 shadow-2xl rounded-2xl p-8 md:p-12 text-white overflow-hidden">
                        
                        <!-- Padrão Blueprint Sutil no Fundo -->
                        <div class="absolute inset-0 bg-[linear-gradient(rgba(255,255,255,0.03)_1px,transparent_1px),linear-gradient(90deg,rgba(255,255,255,0.03)_1px,transparent_1px)] bg-[size:20px_20px]"></div>
                        
                        <div class="relative z-10">
                            <div class="flex items-center space-x-3 mb-8 border-b border-zinc-800 pb-4">
                                <div class="p-2 bg-red-600/20 text-red-500 rounded">
                                    <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"></path></svg>
                                </div>
                                <h3 class="font-playfair text-3xl font-bold">4. MANUAL DE DEFESA (Arma Intelectual)</h3>
                            </div>
                            
                            <p class="text-xl font-light text-zinc-300 leading-relaxed italic border-l-2 border-gold-600 pl-6">
                                "A grande mídia usa a tática de inversão de culpa para transformar o agressor contumaz em vítima e a legítima defesa em crime. Israel não escolheu começar uma guerra em Beirute; o país está neutralizando uma milícia terrorista que ataca civis israelenses diariamente, financiada pelo regime iraniano. Repetir essa manchete é ceder à Engenharia Social Coercitiva de quem odeia os valores do mundo livre e defende silenciosamente o terrorismo."
                            </p>
                        </div>
                    </div>

                    <!-- Fonte do Artigo -->
                    <div class="mt-12 text-right">
                        <a href="https://g1.globo.com/mundo/noticia/2026/06/07/apos-bombardeios-de-israel-a-beirute-ira-lanca-misseis-em-direcao-ao-territorio-israelense-netanyahu-diz-que-havera-resposta.ghtml" target="_blank" rel="noopener noreferrer" class="inline-flex items-center text-sm font-mono text-zinc-500 hover:text-gold-500 transition-colors group">
                            <span>Ler Matéria Original no G1</span>
                            <svg class="w-4 h-4 ml-2 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
                        </a>
                    </div>

                </div>

            </div>

        </div>

    </main>
"""

    with open('modelo-post.html', 'w', encoding='utf-8') as f:
        f.write(head_header + main_content + footer)

update_modelo_post()
