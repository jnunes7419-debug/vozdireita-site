import re

with open("d:/direita_intelectual/analise-cartacapital-peru.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace Page Title
html = re.sub(
    r'<title>.*?</title>',
    '<title>Autópsia: A Falácia da Herança e a Agenda Oculta no Peru | Voz Direita</title>',
    html
)

# Replace Hero Title
html = re.sub(
    r'<h1 class="font-playfair text-5xl md:text-7xl lg:text-8xl font-bold tracking-tight text-white leading-\[1.1\] mb-6 drop-shadow-2xl max-w-4xl">\s*A Fuga do Laboratório Socialista e a Engenharia dos Números\s*</h1>',
    '<h1 class="font-playfair text-5xl md:text-7xl lg:text-8xl font-bold tracking-tight text-white leading-[1.1] mb-6 drop-shadow-2xl max-w-4xl">\n                A Falácia da Herança e a Engenharia Narrativa\n            </h1>',
    html
)

# Replace Hero Subtitle
html = re.sub(
    r'<h2 class="font-jakarta text-xl md:text-2xl text-zinc-300 font-light max-w-3xl leading-relaxed border-l-4 border-gold-500 pl-6 drop-shadow-lg">\s*Como a mídia progressista instrumentaliza números e estatísticas frias para esconder a rejeição massiva ao socialismo entre os expatriados sul-americanos\.\s*</h2>',
    '<h2 class="font-jakarta text-xl md:text-2xl text-zinc-300 font-light max-w-3xl leading-relaxed border-l-4 border-gold-500 pl-6 drop-shadow-lg">\n                Como a mídia de esquerda utiliza Adjetivos de Mancha e a falácia da associação para mascarar a rejeição ao Foro de São Paulo entre os expatriados.\n            </h2>',
    html
)

# Heading 1
html = html.replace('1. A MANCHETE OFICIAL (A Isca)', '1. A MANCHETE OFICIAL E O DOSSIÊ DA FONTE')

# Falsa Premissa
falsa_premissa = """
                        <strong>Dossiê da Fonte:</strong> A CartaCapital, alinhada à estratégia do Foro de São Paulo, escolhe esse tema para mascarar a forte rejeição à esquerda na América Latina. O veículo dilui o fato de que peruanos refugiados no Brasil votam massivamente contra o socialismo, e tenta validar a agenda globalista usando táticas de deslegitimação.
"""
html = re.sub(
    r'<strong>A Falsa Premissa:</strong> A mídia usa uma linguagem asséptica.*?para viver no Brasil\.',
    falsa_premissa.strip(),
    html
)


# Realidade Oculta points
realidade_oculta = """
                        <li><strong>Omissões Estratégicas:</strong> O que o texto não diz? Oculta que os expatriados fugiram justamente do colapso econômico causado por políticas de esquerda, focando apenas na matemática de "11 capitais" para desidratar o impacto político dessa diáspora.</li>
                        <li><strong>Adjetivos de Mancha (Herança e Associação):</strong> Identificamos a falácia lógica de "associação". O texto rotineiramente lembra do parentesco de Keiko para invalidar a direita. Expondo a falácia: O autor não tem argumentos contra as ideias da candidata, por isso recorre à tentativa de destruir sua honra através do passado de terceiros.</li>
                        <li><strong>Identificação de Frames:</strong> A esquerda é sempre emoldurada em tom neutro ou democrático, enquanto a direita sofre o enquadramento pejorativo para isolar os conservadores.</li>
"""
html = re.sub(
    r'<li><strong>O exílio como sintoma:</strong>.*?</li>\s*<li><strong>Filtro Estatístico Asséptico:</strong>.*?</li>\s*<li><strong>O paradoxo do voto progressista:</strong>.*?</li>',
    realidade_oculta,
    html,
    flags=re.DOTALL
)

# Pull Quote
html = re.sub(
    r'"A linguagem asséptica nas matérias não é um acaso, é uma barreira cognitiva projetada para esconder o colapso econômico que obriga a população a fugir\."',
    '"O autor não tem argumentos técnicos contra as ideias da direita, por isso recorre covardemente à tentativa de destruir a honra da candidata através do passado de terceiros."',
    html
)

# Diagnostico
diagnostico = """
                    <p>
                        Desmascaramos a lógica da reportagem: O veículo atua para a manutenção das zonas de influência esquerdista na América do Sul. Ao atacar a herança da oposição e esconder a fuga em massa do "laboratório socialista", eles expõem a hipocrisia de quem defende a democracia apenas quando ela atende aos interesses do Foro de São Paulo.
                    </p>
                    <p>
                        A <strong>Esquerda Neototalitária</strong> aplica essa <strong>Engenharia Social Coercitiva</strong> para isolar os conservadores. A rotulação de "filha de ditador" é um Adjetivo de Mancha criado pelo Progressismo Autoritário para censurar o debate econômico que a esquerda sabe que já perdeu.
                    </p>
"""
html = re.sub(
    r'<p>\s*A estrutura desta manchete e o corpo da reportagem.*?Engenharia Social Coercitiva\.\s*</p>',
    diagnostico,
    html,
    flags=re.DOTALL
)

# Manual
manual = """
                                "Sempre que a mídia chamar um candidato de direita de 'filho de ditador' ou 'ligado a', pergunte: 'Vocês não têm argumentos contra as propostas econômicas, então precisam atacar a família?' Além disso, esconder que os peruanos fugiram da miséria e votaram na direita no Brasil prova apenas uma coisa: quem vive o socialismo na pele, vota contra ele para sobreviver. É pura hipocrisia neototalitária."
"""
html = re.sub(
    r'"A mídia insiste em focar na margem geral apertada.*?covardia jornalística\."',
    manual.strip(),
    html
)

with open("d:/direita_intelectual/analise-cartacapital-peru.html", "w", encoding="utf-8") as f:
    f.write(html)

print("HTML atualizado com protocolo Investigador!")
