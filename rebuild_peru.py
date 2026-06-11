import re

with open("d:/direita_intelectual/analise-carta-capital-pesquisa.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace Page Title
html = re.sub(
    r'<title>.*?</title>',
    '<title>Autópsia: A Fuga do Laboratório Socialista e a Engenharia dos Números | Voz Direita</title>',
    html
)

# Replace Meta Description
html = re.sub(
    r'<meta name="description"\s+content=".*?">',
    '<meta name="description" content="Análise tática sobre a eleição peruana e o voto dos expatriados no Brasil. Entenda como a esquerda usa o filtro estatístico para esconder sua rejeição.">',
    html
)

# Replace Hero Background Image
html = html.replace('assets/lula_flavio_bolsonaro_grafico.webp', 'assets/capa_eleicao_peru.png')
html = html.replace('Imagem de Destaque - Israel e Irã', 'Imagem de Destaque - Eleições Peru')

# Replace Hero Title
html = re.sub(
    r'<h1 class="font-playfair text-5xl md:text-7xl lg:text-8xl font-bold tracking-tight text-white leading-\[1.1\] mb-6 drop-shadow-2xl max-w-4xl">\s*O Falso Empate: A Engenharia Social nas Pesquisas\s*</h1>',
    '<h1 class="font-playfair text-5xl md:text-7xl lg:text-8xl font-bold tracking-tight text-white leading-[1.1] mb-6 drop-shadow-2xl max-w-4xl">\n                A Fuga do Laboratório Socialista e a Engenharia dos Números\n            </h1>',
    html
)

# Replace Hero Subtitle
html = re.sub(
    r'<h2 class="font-jakarta text-xl md:text-2xl text-zinc-300 font-light max-w-3xl leading-relaxed border-l-4 border-gold-500 pl-6 drop-shadow-lg">\s*Como a Esquerda Neototalitária usa manchetes para mascarar a liderança real da oposição e criar uma ilusão de estabilidade para o regime\.\s*</h2>',
    '<h2 class="font-jakarta text-xl md:text-2xl text-zinc-300 font-light max-w-3xl leading-relaxed border-l-4 border-gold-500 pl-6 drop-shadow-lg">\n                Como a mídia progressista instrumentaliza números e estatísticas frias para esconder a rejeição massiva ao socialismo entre os expatriados sul-americanos.\n            </h2>',
    html
)

# Insert Audio Player before 1. A MANCHETE OFICIAL
audio_html = """
                    <!-- Player de Áudio -->
                    <div class="mb-12 p-6 bg-zinc-100 dark:bg-zinc-900/50 rounded-2xl border border-zinc-200 dark:border-zinc-800 shadow-sm flex flex-col sm:flex-row items-center justify-between gap-4">
                        <div class="flex items-center space-x-3">
                            <div class="p-2 bg-gold-600/20 text-gold-600 dark:text-gold-500 rounded-full">
                                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.536 8.464a5 5 0 010 7.072m2.828-9.9a9 9 0 010 12.728M5.586 15H4a1 1 0 01-1-1v-4a1 1 0 011-1h1.586l4.707-4.707C10.923 3.663 12 4.109 12 5v14c0 .891-1.077 1.337-1.707.707L5.586 15z"></path></svg>
                            </div>
                            <div>
                                <h4 class="font-playfair text-lg font-bold text-zinc-900 dark:text-white">Ouvir Dossiê Tático</h4>
                                <p class="text-xs font-mono text-zinc-500">Resumo em áudio da autópsia</p>
                            </div>
                        </div>
                        <audio controls class="w-full sm:w-auto h-10 outline-none" src="audio-peru.mp3"></audio>
                    </div>

                    <h3 class="font-playfair text-3xl font-bold text-zinc-900 dark:text-white mb-6 border-l-4 border-gold-500 pl-4">
"""
html = html.replace('<h3 class="font-playfair text-3xl font-bold text-zinc-900 dark:text-white mb-6 border-l-4 border-gold-500 pl-4">', audio_html, 1)

# Replace Manchete
html = html.replace(
    '"A disputa entre Lula e Flávio Bolsonaro no Espírito Santo, segundo o Real Time Big Data"',
    '"Como está a disputa entre Keiko Fujimori e Sánchez entre peruanos de 11 capitais brasileiras"'
)

# Replace Falsa Premissa
html = re.sub(
    r'O texto foca estrategicamente no cenário de primeiro turno \(35% a 34%\) como um mero "empate técnico", mas oculta da chamada principal a vitória consolidada da oposição no segundo turno \(48% a 43%\)\.',
    'A mídia usa uma linguagem asséptica e matemática para esconder o pânico diante da rejeição expressiva que a esquerda enfrenta entre os expatriados sul-americanos que fugiram da instabilidade econômica para viver no Brasil.',
    html
)

# Replace Realidade Oculta points
realidade_oculta = """
                        <li><strong>O exílio como sintoma:</strong> A narrativa hegemônica cita o histórico familiar de Keiko para criar rejeição moral, mas omite o real motivo pelo qual tantos peruanos estão no Brasil: eles fugiram para buscar trabalho, escapando das políticas instáveis e inflacionárias.</li>
                        <li><strong>Filtro Estatístico Asséptico:</strong> A tática foca excessivamente na contagem de cidades (11 capitais) e em números frios, para que o leitor não perceba que o cidadão trabalhador no exterior vota contra a esquerda de forma sistemática.</li>
                        <li><strong>O paradoxo do voto progressista:</strong> Escondem que o "laboratório socialista" na América Latina gerou uma diáspora massiva, e essa mesma diáspora rejeita violentamente, nas urnas, as ideias que causaram seu próprio êxodo.</li>
"""
html = re.sub(
    r'<li><strong>A manipulação semântica do "empate":</strong>.*?</li>\s*<li><strong>A blindagem do desgaste governista:</strong>.*?</li>\s*<li><strong>Isolamento de dados desfavoráveis:</strong>.*?</li>',
    realidade_oculta,
    html,
    flags=re.DOTALL
)

# Replace image text
html = html.replace('A verdadeira face dos números: A supressão de dados como arma de controle da percepção.', 'A verdadeira face dos números: A supressão das motivações reais do êxodo sul-americano como arma de controle de percepção.')
html = html.replace('Gráfico mostrando a liderança real camuflada pela mídia', 'Capa do artigo da eleição do Peru')

# Replace Pull Quote
html = re.sub(
    r'"A supressão do horizonte no segundo turno não é um erro de edição, é uma arma de controle da percepção\."',
    '"A linguagem asséptica nas matérias não é um acaso, é uma barreira cognitiva projetada para esconder o colapso econômico que obriga a população a fugir."',
    html
)

# Replace Diagnóstico
diagnostico = """
                    <p>
                        A estrutura desta manchete e o corpo da reportagem são a prova cabal da atuação da <strong>Esquerda Neototalitária</strong> e sua manipulação semântica. O <strong>Progressismo Autoritário</strong> precisa, a todo custo, impedir que o público conecte o fracasso da economia socialista latino-americana à forte rejeição que ele sofre nas urnas pelos próprios expatriados que se refugiaram no Brasil.
                    </p>
                    <p>
                        O uso do <strong>Filtro Estatístico Asséptico</strong> anestesia a verdade: a esquerda perde entre aqueles que precisaram abandonar seus países para não passar fome. Transformar isso em um mero balanço numérico entre capitais é pura <strong>Engenharia Social Coercitiva</strong>.
                    </p>
"""
html = re.sub(
    r'<p>\s*A estrutura desta manchete é um exemplo clássico da operação da.*?O leitor é forçado a absorver uma falsa sensação de estabilidade.*?desmotivar a base conservadora\.\s*</p>',
    diagnostico,
    html,
    flags=re.DOTALL
)

# Replace Arma Intelectual
manual = """
                                "A mídia insiste em focar na margem geral apertada para encobrir o fato óbvio: a maioria esmagadora dos peruanos que fugiram pro Brasil votaram na direita. Quem foge do laboratório socialista na América Latina nunca vota no Progressismo Autoritário, vota na direita para sobreviver. Esconder esse fenômeno atrás de matemática fria é pura manipulação neototalitária e covardia jornalística."
"""
html = re.sub(
    r'"A mídia insiste em vender a narrativa do \'empate técnico\', mas a própria pesquisa.*?controle da manchete\."',
    manual,
    html
)

# Replace Link
html = html.replace('https://www.cartacapital.com.br/politica/a-disputa-entre-lula-e-flavio-bolsonaro-no-espirito-santo-segundo-o-real-time-big-data/', 'https://www.cartacapital.com.br/cartaexpressa/como-esta-a-disputa-entre-sanchez-e-keiko-fujimori-entre-peruanos-de-11-capitais-brasileiras/')

with open("d:/direita_intelectual/analise-cartacapital-peru.html", "w", encoding="utf-8") as f:
    f.write(html)

print("HTML reescrito com sucesso!")
