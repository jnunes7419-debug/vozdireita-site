import os

def build_premium_model_post():
    # Extract Head and Header from analise-oglobo-rosa.html
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
            <img src="assets/guerra_pop_1.png" alt="Imagem de Destaque" class="w-full h-full object-cover opacity-60 dark:opacity-40 transform scale-105 transition-transform duration-[10s] hover:scale-100">
            <!-- Overlay de Gradiente Escuro para Leitura -->
            <div class="absolute inset-0 bg-gradient-to-t from-black via-black/60 to-transparent"></div>
            <div class="absolute inset-0 bg-gradient-to-r from-black/80 via-transparent to-transparent"></div>
        </div>

        <!-- Conteúdo do Hero -->
        <div class="relative z-10 max-w-[1200px] w-full px-8 pb-16 md:pb-24">
            
            <!-- Tags e Metadados Acima do Título -->
            <div class="flex items-center space-x-4 mb-6">
                <span class="px-3 py-1 bg-gold-600/90 backdrop-blur-md text-white text-[10px] font-bold uppercase tracking-widest rounded-sm shadow-lg">Guerra Cultural</span>
                <span class="text-zinc-300 text-xs font-mono tracking-wider flex items-center">
                    <svg class="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                    Tempo de Leitura: 6 min
                </span>
            </div>

            <!-- Título Gigante e Impactante -->
            <h1 class="font-playfair text-5xl md:text-7xl lg:text-8xl font-bold tracking-tight text-white leading-[1.1] mb-6 drop-shadow-2xl max-w-4xl">
                O Falso Brilho da Narrativa: A Estratégia do Cavalo de Troia
            </h1>
            
            <!-- Subtítulo / Gancho -->
            <h2 class="font-jakarta text-xl md:text-2xl text-zinc-300 font-light max-w-3xl leading-relaxed border-l-4 border-gold-500 pl-6 drop-shadow-lg">
                Como o progressismo autoritário embala medidas de controle social em falsas pautas de proteção, fragmentando a base conservadora.
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
                            <li class="hover:text-gold-500 cursor-pointer transition-colors flex items-center"><span class="w-1.5 h-1.5 rounded-full bg-gold-500 mr-2"></span> A Narrativa</li>
                            <li class="hover:text-gold-500 cursor-pointer transition-colors flex items-center"><span class="w-1.5 h-1.5 rounded-full bg-zinc-300 dark:bg-zinc-700 mr-2"></span> A Armadilha</li>
                            <li class="hover:text-gold-500 cursor-pointer transition-colors flex items-center"><span class="w-1.5 h-1.5 rounded-full bg-zinc-300 dark:bg-zinc-700 mr-2"></span> O Resumo</li>
                            <li class="hover:text-gold-500 cursor-pointer transition-colors flex items-center"><span class="w-1.5 h-1.5 rounded-full bg-zinc-300 dark:bg-zinc-700 mr-2"></span> O Veredito</li>
                        </ul>
                    </div>

                </div>
            </aside>

            <!-- COLUNA CENTRAL (O Artigo) -->
            <div class="lg:col-span-8 2xl:col-span-7 space-y-12">

                <!-- ARTIGO PRINCIPAL -->
                <!-- Estilização editorial: Primeira letra (Drop Cap) enorme -->
                <article class="prose prose-zinc dark:prose-invert max-w-none text-lg md:text-xl leading-relaxed font-jakarta font-light text-zinc-800 dark:text-zinc-300 
                    prose-p:mb-8 prose-strong:text-zinc-900 dark:prose-strong:text-white prose-strong:font-semibold">
                    
                    <p class="first-letter:text-7xl first-letter:font-playfair first-letter:font-bold first-letter:text-gold-600 first-letter:float-left first-letter:mr-4 first-letter:-mt-2 first-letter:leading-none">
                        O cenário político nacional, sob a ótica da contrainteligência, demonstra que as investidas ideológicas da <strong>Esquerda Neototalitária</strong> frequentemente se utilizam de pautas de gênero para induzir parlamentares da base de oposição a servirem de vetores involuntários de infiltração. O protocolo de medidas que superficialmente parecem proteger o cidadão, muitas vezes escondem um núcleo de ação destrutiva. A análise de narrativas exige um ceticismo estrutural, não apenas sobre o que está sendo dito, mas sobre o que está sendo convenientemente omitido pelos grandes veículos de comunicação.
                    </p>

                    <p>
                        Quando observamos o comportamento da mídia de massa, nota-se um alinhamento quase orquestral. A manobra legislativa articula-se em torno de uma armadilha tática que classificamos como o dilema de "Cruz e Espada". Lideranças centrais da oposição conservadora são submetidas a escolhas impossíveis: se validarem a medida, endossam o punitivismo estético e a humilhação pública do homem comum antes de qualquer julgamento, alienando sua própria base; se propuserem um debate técnico sobre sua ineficácia, são sumariamente linchados pela imprensa hegemônica sob o rótulo de "misóginos".
                    </p>

                    <!-- Pull Quote Elegante -->
                    <blockquote class="relative my-12 p-8 md:p-12 text-center bg-zinc-100/50 dark:bg-zinc-900/30 rounded-3xl border border-zinc-200/50 dark:border-white/5 shadow-inner">
                        <svg class="absolute top-4 left-6 w-12 h-12 text-gold-500/20" fill="currentColor" viewBox="0 0 24 24"><path d="M14.017 21v-7.391c0-5.704 3.731-9.57 8.983-10.609l.995 2.151c-2.432.917-3.995 3.638-3.995 5.849h4v10h-9.983zm-14.017 0v-7.391c0-5.704 3.748-9.57 9-10.609l.996 2.151c-2.433.917-3.996 3.638-3.996 5.849h3.983v10h-9.983z"/></svg>
                        <p class="font-playfair text-2xl md:text-3xl font-medium text-zinc-900 dark:text-gold-400 italic mb-0 leading-tight">
                            "A assimetria punitiva não é um erro do sistema, mas uma funcionalidade cuidadosamente implementada pela Hegemonia do Jornalismo."
                        </p>
                    </blockquote>

                    <p>
                        Essa obsessão legislativa por performáticas punitivas cinde a espinha dorsal do devido processo legal e abre margem para o relativismo da presunção de inocência. O uso de coloração cromática vexatória em um dispositivo de rastreamento não cumpre nenhuma função técnica de segurança pública; atua estritamente como uma marca de execração pública. O <strong>feminismo totalitário</strong>, encastelado na burocracia estatal e amplificado pela mídia de massa, promove a rotulação simbólica do acusado para habituar a opinião pública a sanções cautelares humilhantes.
                    </p>

                    <p>
                        A falsidade da pauta protetiva revela-se quando confrontada com a leniência dispensada pelo sistema judicial a criminosas confessas do sexo feminino em casos de extrema gravidade. Enquanto se propõe marcar esteticamente o homem comum no início de investigações preliminares, criminosas notórias recebem progressão de regime, saídas temporárias no Dia das Mães e tratamento humanizado em reportagens de domingo.
                    </p>

                    <p>
                        Dessa forma, o verdadeiro objetivo dessas propostas não é a defesa do inocente ou a redução da criminalidade real, mas a institucionalização da desmoralização masculina e a erosão do princípio constitucional da isonomia. Cabe a nós, analistas da guerra cultural, desmascarar a <strong>Engenharia Social Coercitiva</strong> que se esconde sob as boas intenções de medidas midiáticas, protegendo o cidadão de direita da armadilha neototalitária. O trabalho de desconstrução de narrativas é essencial para não sermos manipulados pelas falsas equivalências da grande mídia.
                    </p>

                </article>

                <!-- BLOCO PREMIUM: RESUMO E ANÁLISE -->
                <div class="mt-20 space-y-12">
                    
                    <!-- Resumo Box -->
                    <div class="relative bg-white dark:bg-zinc-900/80 border-t-4 border-gold-600 shadow-2xl rounded-b-2xl p-8 md:p-12 overflow-hidden">
                        <div class="absolute top-0 right-0 p-4 opacity-5">
                            <svg class="w-32 h-32" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-2h2v2zm0-4h-2V7h2v6z"/></svg>
                        </div>
                        <h3 class="relative z-10 font-playfair text-3xl font-bold text-zinc-900 dark:text-white mb-6 flex items-center">
                            <span class="w-8 h-px bg-gold-600 mr-4 hidden sm:block"></span> 
                            Resumo do Artigo Original
                        </h3>
                        <p class="relative z-10 text-lg md:text-xl leading-relaxed font-light text-zinc-700 dark:text-zinc-300">
                            A notícia ou artigo original apresenta a medida como um avanço na proteção social, utilizando um tom emotivo e focando exclusivamente nos benefícios aparentes da proposta legislativa. As reportagens evitam mencionar as implicações legais da presunção de inocência e destacam, repetidamente, o "caráter educativo" da punição estética antes mesmo do julgamento final do acusado.
                        </p>
                    </div>

                    <!-- Análise Box (Glassmorphism Escuro) -->
                    <div class="relative bg-zinc-900 dark:bg-black border border-zinc-800 dark:border-zinc-800/50 shadow-2xl rounded-2xl p-8 md:p-12 text-white overflow-hidden">
                        
                        <!-- Padrão Blueprint Sutil no Fundo -->
                        <div class="absolute inset-0 bg-[linear-gradient(rgba(255,255,255,0.03)_1px,transparent_1px),linear-gradient(90deg,rgba(255,255,255,0.03)_1px,transparent_1px)] bg-[size:20px_20px]"></div>
                        
                        <div class="relative z-10">
                            <div class="flex items-center space-x-3 mb-8 border-b border-zinc-800 pb-4">
                                <div class="p-2 bg-red-600/20 text-red-500 rounded">
                                    <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
                                </div>
                                <h3 class="font-playfair text-3xl font-bold">Autópsia Tática</h3>
                            </div>
                            
                            <ul class="space-y-6 text-lg font-light text-zinc-300">
                                <li class="flex items-start">
                                    <span class="text-gold-500 mr-3 mt-1">◆</span>
                                    <div>
                                        <strong class="text-white block mb-1">Falsa Preocupação Social</strong>
                                        O artigo original oculta que a sanção é aplicada antes do devido processo legal, destruindo a presunção de inocência sob o pretexto de urgência social.
                                    </div>
                                </li>
                                <li class="flex items-start">
                                    <span class="text-gold-500 mr-3 mt-1">◆</span>
                                    <div>
                                        <strong class="text-white block mb-1">Omissão Estratégica</strong>
                                        A mídia falha propositalmente em contrastar o tratamento rigoroso exigido aqui com a brandura aplicada a crimes hediondos cometidos por mulheres, criando o padrão <strong>"dois pesos, duas medidas"</strong>.
                                    </div>
                                </li>
                                <li class="flex items-start">
                                    <span class="text-gold-500 mr-3 mt-1">◆</span>
                                    <div>
                                        <strong class="text-white block mb-1">Engenharia Social em Ação</strong>
                                        Utiliza-se a estética (cor rosa) não para segurança, mas como ferramenta de <strong>humilhação pública</strong> aprovada pelo Estado.
                                    </div>
                                </li>
                            </ul>
                        </div>
                    </div>

                </div>

            </div>

        </div>

    </main>
"""

    with open('modelo-post.html', 'w', encoding='utf-8') as f:
        f.write(head_header + main_content + footer)

build_premium_model_post()
