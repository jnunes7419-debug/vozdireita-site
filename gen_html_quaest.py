import re

with open("d:/direita_intelectual/analise-carta-capital-pesquisa.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace Page Title
html = re.sub(
    r'<title>.*?</title>',
    '<title>Autópsia: A Engenharia Social nas Pesquisas Fatiadas | Voz Direita</title>',
    html
)

# Replace Meta Tags
html = re.sub(
    r'<meta name="description"\s+content=".*?">',
    '<meta name="description" content="Análise tática de como a mídia usa recortes estatísticos hiper-específicos para fabricar vitórias da esquerda e esconder a rejeição ao governo.">',
    html
)
html = re.sub(
    r'<meta name="keywords"\s+content=".*?">',
    '<meta name="keywords" content="Pesquisa Quaest, Eleições 2026, Engenharia Social Coercitiva, Esquerda Neototalitária, G1, Manipulação de Pesquisas, Efeito Manada, Jander Nunes, Voz Direita">',
    html
)

# Replace Hero Background Image
html = html.replace('assets/lula_flavio_bolsonaro_grafico.webp', 'assets/capa_quaest_eleicoes.png')
html = html.replace('Imagem de Destaque - Israel e Irã', 'Imagem de Destaque - Pesquisa Quaest')

# Replace Hero Title
html = re.sub(
    r'<h1 class="font-playfair text-5xl md:text-7xl lg:text-8xl font-bold tracking-tight text-white leading-\[1.1\] mb-6 drop-shadow-2xl max-w-4xl">.*?</h1>',
    '<h1 class="font-playfair text-5xl md:text-7xl lg:text-8xl font-bold tracking-tight text-white leading-[1.1] mb-6 drop-shadow-2xl max-w-4xl">\n                A Fabricação de Consenso: O Filtro Estatístico do G1\n            </h1>',
    html,
    flags=re.DOTALL
)

# Replace Hero Subtitle
html = re.sub(
    r'<h2 class="font-jakarta text-xl md:text-2xl text-zinc-300 font-light max-w-3xl leading-relaxed border-l-4 border-gold-500 pl-6 drop-shadow-lg">.*?</h2>',
    '<h2 class="font-jakarta text-xl md:text-2xl text-zinc-300 font-light max-w-3xl leading-relaxed border-l-4 border-gold-500 pl-6 drop-shadow-lg">\n                Como a mídia de esquerda fatia pesquisas de intenção de voto para criar manchetes vitoriosas e forjar um "efeito manada" artificial.\n            </h2>',
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
                        <audio controls class="w-full sm:w-auto h-10 outline-none" src="audio-quaest.mp3"></audio>
                    </div>

                    <h3 class="font-playfair text-3xl font-bold text-zinc-900 dark:text-white mb-6 border-l-4 border-gold-500 pl-4">
                        1. A MANCHETE OFICIAL E O DOSSIÊ DA FONTE
                    </h3>
"""
html = re.sub(r'<h3 class="font-playfair text-3xl font-bold text-zinc-900 dark:text-white mb-6 border-l-4 border-gold-500 pl-4">\s*1\. A MANCHETE OFICIAL \(A Isca\)\s*</h3>', audio_html, html)


# Replace Manchete
html = html.replace(
    '"A disputa entre Lula e Flávio Bolsonaro no Espírito Santo, segundo o Real Time Big Data"',
    '"Quaest: Entre eleitores independentes, Lula passa Flávio Bolsonaro e abre 13 pontos de vantagem no 2º turno"'
)

# Replace Falsa Premissa
falsa_premissa = """
                        <strong>Dossiê da Fonte:</strong> O G1 atua como correia de transmissão do governo. Ao destacar um recorte hiper-específico (eleitores independentes) na manchete, o portal tenta criar uma narrativa de que a direita está perdendo força. O objetivo é fabricar um consenso falso de vitória esquerdista.
"""
html = re.sub(
    r'<strong>A Falsa Premissa:</strong>.*?</p>',
    falsa_premissa.strip() + '\n                    </p>',
    html,
    flags=re.DOTALL
)

# Realidade Oculta points
realidade_oculta = """
                        <li><strong>Filtro Estatístico a Favor do Sistema:</strong> Eles fatiaram a pesquisa para destacar o único grupo onde o governo teve uma variação "positiva" clara, escondendo na manchete o cenário geral desastroso de desaprovação.</li>
                        <li><strong>Identificação de Frames e Adjetivos de Mancha:</strong> A matéria associa a queda da oposição a narrativas de "bancos" e "Trump", criando relações de causa e efeito artificiais. A intenção é óbvia: desgastar a direita com adjetivos de mancha antes mesmo do debate de ideias.</li>
                        <li><strong>Engenharia Social do Efeito Manada:</strong> A esquerda neototalitária sabe que parte do eleitorado "independente" vota em quem aparenta estar ganhando. A manchete é uma ferramenta de recrutamento para gerar um efeito manada psicológico.</li>
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
    '"Se a mídia precisa garimpar um único recorte estatístico para encontrar uma boa notícia, é porque o governo já faliu."',
    html
)

# Diagnostico
diagnostico = """
                    <p>
                        A estrutura desta manchete é um exemplo clássico da operação da <strong>Esquerda Neototalitária</strong>. Eles aplicam a <strong>Engenharia Social Coercitiva</strong> através da estatística fatiada: ocultam a rejeição generalizada da população e dão um megafone para um recorte restrito ("independentes") a fim de forçar a percepção de que a oposição está encolhendo.
                    </p>
                    <p>
                        Ao instrumentalizar o instituto de pesquisa, o <strong>Progressismo Autoritário</strong> transforma dados em propaganda de guerra psicológica, com o único propósito de desmobilizar e rachar a base conservadora.
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
                                "A mídia pega um recorte estatístico minúsculo para fabricar uma manchete de vitória para o governo, enquanto esconde o cenário desastroso da aprovação real. Se eles precisam fatiar a pesquisa para encontrar uma boa notícia, é porque o sistema está colapsando. É apenas a velha engenharia social esquerdista tentando forjar um efeito manada."
"""
html = re.sub(
    r'"A mídia insiste em vender a narrativa do \'empate técnico\',.*?controle da manchete\."',
    manual.strip(),
    html,
    flags=re.DOTALL
)

# Replace Link
html = html.replace('https://www.cartacapital.com.br/politica/a-disputa-entre-lula-e-flavio-bolsonaro-no-espirito-santo-segundo-o-real-time-big-data/', 'https://g1.globo.com/politica/eleicoes/2026/noticia/2026/06/10/quaest-eleitores-independentes.ghtml')

with open("d:/direita_intelectual/analise-g1-quaest.html", "w", encoding="utf-8") as f:
    f.write(html)

print("HTML Quaest gerado com sucesso!")
