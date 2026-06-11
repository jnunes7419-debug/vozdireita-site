import re

with open("d:/direita_intelectual/analise-carta-capital-pesquisa.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace Page Title
html = re.sub(
    r'<title>.*?</title>',
    '<title>Autópsia: A Hegemonia Globalista e o Ataque à Soberania | Voz Direita</title>',
    html
)

# Replace Meta Tags
html = re.sub(
    r'<meta name="description"\s+content=".*?">',
    '<meta name="description" content="Análise tática de como a mídia usa o esporte para atacar líderes conservadores que defendem a soberania nacional.">',
    html
)
html = re.sub(
    r'<meta name="keywords"\s+content=".*?">',
    '<meta name="keywords" content="Donald Trump, FIFA, Gianni Infantino, Esquerda Neototalitária, Progressismo Autoritário, L\'Équipe, G1, Soberania Nacional, Globalismo, Voz Direita">',
    html
)

# Replace Hero Background Image
html = html.replace('assets/lula_flavio_bolsonaro_grafico.webp', 'assets/capa_fifa_trump.png')
html = html.replace('Imagem de Destaque - Israel e Irã', 'Imagem de Destaque - FIFA Trump')

# Replace Hero Title
html = re.sub(
    r'<h1 class="font-playfair text-5xl md:text-7xl lg:text-8xl font-bold tracking-tight text-white leading-\[1.1\] mb-6 drop-shadow-2xl max-w-4xl">.*?</h1>',
    '<h1 class="font-playfair text-5xl md:text-7xl lg:text-8xl font-bold tracking-tight text-white leading-[1.1] mb-6 drop-shadow-2xl max-w-4xl">\n                A Arma do Esporte: O Ataque Globalista à Soberania\n            </h1>',
    html,
    flags=re.DOTALL
)

# Replace Hero Subtitle
html = re.sub(
    r'<h2 class="font-jakarta text-xl md:text-2xl text-zinc-300 font-light max-w-3xl leading-relaxed border-l-4 border-gold-500 pl-6 drop-shadow-lg">.*?</h2>',
    '<h2 class="font-jakarta text-xl md:text-2xl text-zinc-300 font-light max-w-3xl leading-relaxed border-l-4 border-gold-500 pl-6 drop-shadow-lg">\n                Como a mídia neototalitária instrumentaliza casos isolados no futebol para demonizar o controle de fronteiras e atacar líderes conservadores.\n            </h2>',
    html,
    flags=re.DOTALL
)

# Insert Audio Player
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
                        <audio controls class="w-full sm:w-auto h-10 outline-none" src="audio-fifa-trump.mp3"></audio>
                    </div>

                    <h3 class="font-playfair text-3xl font-bold text-zinc-900 dark:text-white mb-6 border-l-4 border-gold-500 pl-4">
                        1. A MANCHETE OFICIAL E O DOSSIÊ DA FONTE
                    </h3>
"""
html = re.sub(r'<h3 class="font-playfair text-3xl font-bold text-zinc-900 dark:text-white mb-6 border-l-4 border-gold-500 pl-4">\s*1\. A MANCHETE OFICIAL \(A Isca\)\s*</h3>', audio_html, html)


# Replace Manchete
html = html.replace(
    '"A disputa entre Lula e Flávio Bolsonaro no Espírito Santo, segundo o Real Time Big Data"',
    '"Gianni Infantino é chamado de fantoche de Trump no jornal L\'Équipe"'
)

# Replace Falsa Premissa
falsa_premissa = """
                        <strong>Dossiê da Fonte:</strong> O G1 ecoa a narrativa globalista do jornal francês L'Équipe para construir a imagem de Donald Trump como um tirano e do presidente da FIFA como um mero "fantoche". A verdadeira intenção é deslegitimar a soberania americana sobre suas próprias fronteiras, usando o esporte como chantagem moral.
"""
html = re.sub(
    r'<strong>A Falsa Premissa:</strong>.*?</p>',
    falsa_premissa.strip() + '\n                    </p>',
    html,
    flags=re.DOTALL
)

# Realidade Oculta points
realidade_oculta = """
                        <li><strong>Adjetivos de Mancha e Desumanização:</strong> O uso do termo "fantoche" é uma tática primária de deslegitimação. Ao invés de debater a validade de uma política migratória, a mídia ataca a reputação das lideranças, forçando a ideia de subserviência e autoritarismo.</li>
                        <li><strong>Omissão da Soberania:</strong> A matéria romantiza a situação do árbitro somali, mas omite o direito inalienável de qualquer nação de controlar quem entra em seu território. Segurança nacional é rebaixada a "capricho".</li>
                        <li><strong>Apelo Emocional Barato:</strong> Usar o futebol, uma paixão global, como escudo para impor pautas de imigração sem controle é pura Engenharia Social Coercitiva. Eles transformam um caso burocrático em um drama de direitos humanos.</li>
"""
html = re.sub(
    r'<li><strong>A manipulação semântica do "empate":</strong>.*?</li>\s*<li><strong>A blindagem do desgaste governista:</strong>.*?</li>\s*<li><strong>Isolamento de dados desfavoráveis:</strong>.*?</li>',
    realidade_oculta,
    html,
    flags=re.DOTALL
)

# Remove the inner image in the body from the model if it exists
html = re.sub(
    r'<div class="my-10 space-y-3">\s*<div class="border border-zinc-200.*?</div>\s*<p class="text-xs text-zinc-500 font-mono tracking-wide text-center">.*?</p>\s*</div>',
    '',
    html,
    flags=re.DOTALL
)

# Replace Pull Quote
html = re.sub(
    r'"A supressão do horizonte no segundo turno não é um erro de edição, é uma arma de controle da percepção\."',
    '"A mídia não se importa com árbitros ou atletas; eles se importam em minar líderes conservadores usando a emoção do esporte como arma de chantagem moral."',
    html
)

# Diagnostico
diagnostico = """
                    <p>
                        Esta reportagem é um claro exercício de <strong>Esquerda Neototalitária</strong> em nível global. Através do jornal francês e ecoado pela mídia nacional, o <strong>Progressismo Autoritário</strong> tenta impor a ideia de que o evento esportivo está acima das leis de um país soberano.
                    </p>
                    <p>
                        A <strong>Engenharia Social Coercitiva</strong> se manifesta na inversão de culpa: o país que protege suas fronteiras é chamado de "opressivo", e qualquer entidade que colabore com ele (a FIFA) é rotulada de "fantoche". Eles utilizam o soft power do esporte para promover o enfraquecimento das nações.
                    </p>
"""
html = re.sub(
    r'<p>\s*A estrutura desta manchete é um exemplo clássico da operação da.*?desmotivar a base conservadora\.\s*</p>',
    diagnostico,
    html,
    flags=re.DOTALL
)

# Manual
manual = """
                                "Quando a mídia tentar te comover com a história do árbitro barrado, responda: 'Um país sem fronteiras seguras não é um país. Nenhuma Copa do Mundo está acima da soberania e da segurança nacional. Chamar o controle migratório de tirania é apenas o progressismo globalista usando o esporte para enfraquecer o Ocidente.'"
"""
html = re.sub(
    r'"A mídia insiste em vender a narrativa do \'empate técnico\',.*?controle da manchete\."',
    manual.strip(),
    html,
    flags=re.DOTALL
)

# Replace Link
html = html.replace('https://www.cartacapital.com.br/politica/a-disputa-entre-lula-e-flavio-bolsonaro-no-espirito-santo-segundo-o-real-time-big-data/', 'https://g1.globo.com/mundo/noticia/2026/06/10/presidente-da-fifa-e-retratado-como-fantoche-de-trump-em-jornal-frances.ghtml')

with open("d:/direita_intelectual/analise-g1-fifa-trump.html", "w", encoding="utf-8") as f:
    f.write(html)

print("HTML FIFA gerado com sucesso!")
