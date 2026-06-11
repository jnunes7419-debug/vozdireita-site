import os

def extract_head_header_footer():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Get up to header
    header_end = content.find('</header>') + len('</header>')
    head_header = content[:header_end]
    
    # Fix the button for "Voltar" in the header since index.html has links to different things
    # Wait, analise-oglobo-rosa.html has a specific header for internal pages (with a Back button)
    return head_header

def build_model_post():
    with open('analise-oglobo-rosa.html', 'r', encoding='utf-8') as f:
        analise = f.read()
    
    # Extract Head and Header from analise-oglobo-rosa.html
    header_end = analise.find('</header>') + len('</header>')
    head_header = analise[:header_end]
    
    # Extract Footer from analise-oglobo-rosa.html
    footer_start_idx = analise.find('<!-- FOOTER (RODAPÉ) -->')
    footer = analise[footer_start_idx:]
    
    main_content = """

    <!-- CABEÇALHO DO POST (HERO) -->
    <section class="relative pt-32 pb-16 w-full overflow-hidden bg-slate-50 dark:bg-zinc-950">

        <!-- Padrão Sutil de Grade Linear -->
        <div
            class="absolute inset-0 z-0 bg-[linear-gradient(rgba(0,0,0,0.015)_1px,transparent_1px),linear-gradient(90deg,rgba(0,0,0,0.015)_1px,transparent_1px)] dark:bg-[linear-gradient(rgba(255,255,255,0.015)_1px,transparent_1px),linear-gradient(90deg,rgba(255,255,255,0.015)_1px,transparent_1px)] bg-[size:30px_30px] opacity-75">
        </div>
        <div class="absolute inset-0 bg-gradient-to-t from-slate-50 via-slate-50/90 to-slate-50 dark:from-intel-950 dark:via-zinc-950/95 dark:to-zinc-950">
        </div>

        <div class="relative z-10 max-w-[1200px] w-full mx-auto px-8 space-y-6">
            
            <!-- Título -->
            <h1 class="font-playfair text-4xl sm:text-5xl md:text-6xl font-bold tracking-tight text-zinc-900 dark:text-white leading-tight">
                Título Oficial da Análise: Desconstruindo a Narrativa
            </h1>
            
            <!-- Subtítulo (SEO Otimizado) -->
            <h2 class="font-playfair text-xl md:text-2xl text-zinc-700 dark:text-stone-300 italic font-light max-w-4xl leading-relaxed">
                Neste subtítulo estrategicamente posicionado, incluímos as palavras-chave principais do tema, ajudando na indexação e fornecendo um gancho poderoso sobre a engenharia social abordada.
            </h2>

        </div>
    </section>

    <!-- CORPO DO POST -->
    <main class="relative z-20 flex-grow bg-slate-50 dark:bg-intel-950 transition-colors duration-300">
        
        <div class="max-w-[1200px] w-full px-8 mx-auto pb-16 space-y-12">
            
            <!-- Imagem de Destaque -->
            <div class="w-full relative aspect-video bg-zinc-200 dark:bg-zinc-900 rounded-2xl overflow-hidden shadow-xl border border-zinc-200 dark:border-white/10">
                <!-- Imagem Placeholder -->
                <img src="assets/guerra_pop_1.png" alt="Imagem de Destaque" class="w-full h-full object-cover">
            </div>

            <!-- Assinatura Jander Nunes -->
            <div class="flex items-center space-x-4 border-b border-zinc-200 dark:border-white/10 pb-8">
                <img src="assets/jander_nunes_profile.png" alt="Jander Nunes" class="w-14 h-14 rounded-full border border-zinc-200 dark:border-white/10 shadow-sm object-cover">
                <div>
                    <p class="font-bold text-lg text-zinc-900 dark:text-white font-playfair tracking-wide">Por Jander Nunes</p>
                    <p class="text-xs uppercase tracking-widest text-zinc-500 dark:text-zinc-400 font-mono">Analista de Inteligência e Mentor</p>
                </div>
            </div>

            <!-- ARTIGO (Mínimo 500 palavras formatadas) -->
            <article class="prose prose-zinc dark:prose-invert max-w-none text-base md:text-lg leading-relaxed font-jakarta font-light text-zinc-700 dark:text-stone-300 space-y-8">
                
                <p>
                    O cenário político nacional, sob a ótica da contrainteligência, demonstra que as investidas ideológicas da <strong>Esquerda Neototalitária</strong> frequentemente se utilizam de pautas de gênero para induzir parlamentares da base de oposição a servirem de vetores involuntários de infiltração. O protocolo de medidas que superficialmente parecem proteger o cidadão, muitas vezes escondem um núcleo de ação destrutiva. A análise de narrativas exige um ceticismo estrutural, não apenas sobre o que está sendo dito, mas sobre o que está sendo convenientemente omitido pelos grandes veículos de comunicação.
                </p>

                <p>
                    Quando observamos o comportamento da mídia de massa, nota-se um alinhamento quase orquestral. A manobra legislativa articula-se em torno de uma armadilha tática que classificamos como o dilema de "Cruz e Espada". Lideranças centrais da oposição conservadora são submetidas a escolhas impossíveis: se validarem a medida, endossam o punitivismo estético e a humilhação pública do homem comum antes de qualquer julgamento, alienando sua própria base; se propuserem um debate técnico sobre sua ineficácia, são sumariamente linchados pela imprensa hegemônica sob o rótulo de "misóginos".
                </p>

                <p>
                    Essa obsessão legislativa por performáticas punitivas cinde a espinha dorsal do devido processo legal e abre margem para o relativismo da presunção de inocência. O uso de coloração cromática vexatória em um dispositivo de rastreamento não cumpre nenhuma função técnica de segurança pública; atua estritamente como uma marca de execração pública. O <strong>feminismo totalitário</strong>, encastelado na burocracia estatal e amplificado pela mídia de massa, promove a rotulação simbólica do acusado para habituar a opinião pública a sanções cautelares humilhantes.
                </p>

                <p>
                    A falsidade da pauta protetiva revela-se quando confrontada com a leniência dispensada pelo sistema judicial a criminosas confessas do sexo feminino em casos de extrema gravidade. Enquanto se propõe marcar esteticamente o homem comum no início de investigações preliminares, criminosas notórias recebem progressão de regime, saídas temporárias no Dia das Mães e tratamento humanizado em reportagens de domingo. Essa assimetria punitiva não é um erro do sistema, mas uma funcionalidade cuidadosamente implementada pela <strong>Hegemonia do Jornalismo</strong> para subverter valores morais objetivos e instalar um relativismo penal sistêmico.
                </p>

                <p>
                    Dessa forma, o verdadeiro objetivo dessas propostas não é a defesa do inocente ou a redução da criminalidade real, mas a institucionalização da desmoralização masculina e a erosão do princípio constitucional da isonomia. Cabe a nós, analistas da guerra cultural, desmascarar a <strong>Engenharia Social Coercitiva</strong> que se esconde sob as boas intenções de medidas midiáticas, protegendo o cidadão de direita da armadilha neototalitária. O trabalho de desconstrução de narrativas é essencial para não sermos manipulados pelas falsas equivalências da grande mídia.
                </p>

            </article>

            <!-- RESUMO E ANÁLISE -->
            <div class="mt-16 bg-slate-100 dark:bg-zinc-900/50 border border-zinc-200 dark:border-zinc-800 rounded-2xl p-8 shadow-sm">
                
                <h3 class="font-playfair text-2xl font-bold text-zinc-900 dark:text-white mb-4 border-b border-zinc-300 dark:border-zinc-700 pb-2">
                    Resumo do Artigo Original
                </h3>
                <p class="text-base md:text-lg leading-relaxed font-light text-zinc-700 dark:text-stone-300 mb-8">
                    A notícia ou artigo original apresenta a medida como um avanço na proteção social, utilizando um tom emotivo e focando exclusivamente nos benefícios aparentes da proposta legislativa. As reportagens evitam mencionar as implicações legais da presunção de inocência e destacam, repetidamente, o "caráter educativo" da punição estética antes mesmo do julgamento final do acusado.
                </p>

                <h3 class="font-playfair text-2xl font-bold text-zinc-900 dark:text-white mb-4 border-b border-zinc-300 dark:border-zinc-700 pb-2">
                    Análise (Autópsia Tática)
                </h3>
                <ul class="space-y-4 text-base md:text-lg leading-relaxed font-light text-zinc-700 dark:text-stone-300">
                    <li>
                        <strong>Falsa Preocupação Social:</strong> O artigo original oculta que a sanção é aplicada antes do devido processo legal, destruindo a presunção de inocência sob o pretexto de urgência social.
                    </li>
                    <li>
                        <strong>Omissão Estratégica:</strong> A mídia falha propositalmente em contrastar o tratamento rigoroso exigido aqui com a brandura aplicada a crimes hediondos cometidos por mulheres, criando o padrão <strong>"dois pesos, duas medidas"</strong>.
                    </li>
                    <li>
                        <strong>Engenharia Social em Ação:</strong> Utiliza-se a estética (cor rosa) não para segurança, mas como ferramenta de <strong>humilhação pública</strong> aprovada pelo Estado.
                    </li>
                </ul>

            </div>

        </div>

    </main>
"""

    with open('modelo-post.html', 'w', encoding='utf-8') as f:
        f.write(head_header + main_content + footer)

build_model_post()
