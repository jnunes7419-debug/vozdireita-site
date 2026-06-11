import re

with open("d:/direita_intelectual/analise-oglobo-rosa.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Title and Meta
html = re.sub(
    r'<title>.*?</title>',
    '<title>Autópsia: A Fuga do Laboratório Socialista e a Engenharia dos Números | Voz Direita</title>',
    html
)
html = re.sub(
    r'<meta name="description"\s+content=".*?">',
    '<meta name="description"\n        content="Análise tática sobre a eleição peruana e o voto dos expatriados no Brasil. Entenda como a esquerda usa o filtro estatístico para esconder sua rejeição.">',
    html
)

# 2. Tag de Alerta
html = html.replace('ALVO: O GLOBO BRASIL', 'ALVO: CARTA CAPITAL')

# 3. Título Editorial
html = re.sub(
    r'A Armadilha do Cavalo de Troia: <br class="hidden md:inline"><span[^>]*>O PL 1811/2026 e a Divisão da Base Conservadora</span>',
    'A Fuga do Laboratório Socialista: <br class="hidden md:inline"><span class="text-transparent bg-clip-text bg-gradient-to-r from-red-600 to-gold-400">O Filtro Estatístico da Esquerda Neototalitária</span>',
    html
)

# 4. Subtítulo
html = re.sub(
    r'Como o progressismo autoritário e a performática de gênero são instrumentalizados para cindir a\s*direita e institucionalizar a desmoralização masculina\.',
    'Como a mídia progressista instrumentaliza números para esconder a rejeição massiva ao socialismo entre os expatriados sul-americanos.',
    html
)

# 5. Metadados
html = html.replace('07 de Junho,', '10 de Junho,')

# ADD AUDIO PLAYER IN HERO SECTION
audio_tag = '\n                <!-- Player de Áudio -->\n                <div class="mt-6 w-full max-w-2xl">\n                    <span class="text-[10px] uppercase font-mono text-gold-500 font-bold mb-1 block">Ouvir Dossiê Tático:</span>\n                    <audio controls class="w-full h-10 rounded-md shadow-lg outline-none" src="audio-peru.mp3"></audio>\n                </div>\n'
html = html.replace('<!-- Metadados -->', audio_tag + '\n                <!-- Metadados -->')

# 6. Passo 1: Manchete e Falsa Premissa
html = html.replace('O GLOBO NOTÍCIAS', 'CARTA CAPITAL')
html = html.replace('20/04/2026', '10/06/2026')
html = html.replace('assets/tornozeleira_rosa.webp', 'assets/capa_eleicao_peru.png')
html = html.replace('Monitoramento de Tornozeleira Rosa', 'Urna e Bandeira do Peru com Alerta')

html = re.sub(
    r'"Tornozeleira rosa: Projeto de lei busca padronizar monitoramento de acusados de\s*violência contra a mulher"',
    '"Como está a disputa entre Keiko Fujimori e Sánchez entre peruanos de 11 capitais brasileiras"',
    html
)
html = re.sub(
    r'A imprensa hegemônica e defensores da proposta sugerem que alterar a cor\s*do dispositivo eletrônico de rastreamento é uma resposta dissuasória eficaz contra\s*agressores, quando na verdade estetiza e disfarça a falência penal real\.',
    'A mídia usa uma linguagem asséptica e matemática para esconder o pânico diante da rejeição expressiva que a esquerda enfrenta entre os expatriados sul-americanos que fugiram da instabilidade econômica.',
    html
)

# 7. Passo 2 & 3: Leitura Raio-X
leitura_raio_x = '''"A apuração dos votos no segundo turno da eleição presidencial no Peru segue acirrada na noite desta quarta-feira 10, com uma vantagem de cerca de dez mil votos a favor de Roberto Sánchez (esquerda) na disputa contra Keiko Fujimori (direita). <span class="group relative inline cursor-pointer border-b-2 border-red-500/60 dark:border-red-500/40 hover:border-red-600 dark:hover:border-red-400 pb-0.5 font-semibold text-red-600 dark:text-red-500 transition-colors">No Brasil, por outro lado, a filha do ex-ditador Alberto Fujimori lidera<!-- Tooltip --><span class="pointer-events-none absolute bottom-full left-1/2 -translate-x-1/2 mb-3 w-80 p-4 bg-zinc-950/95 dark:bg-[#0a0f18]/90 border border-red-500/30 dark:border-white/10 backdrop-blur-md rounded-xl text-xs text-stone-300 font-jakarta leading-relaxed shadow-2xl opacity-0 translate-y-2 group-hover:opacity-100 group-hover:translate-y-0 transition-all duration-300 z-50 normal-case not-italic text-left font-sans">Omissão de Motivo (Exílio como Sintoma): Eles citam o nome do pai para criar rejeição, mas omitem o real motivo: quem fugiu do país foi para buscar trabalho no Brasil, fugindo das políticas instáveis e inflacionárias. A "direita" aqui representa a sobrevivência para eles.<span class="absolute top-full left-1/2 -translate-x-1/2 border-8 border-transparent border-t-zinc-950/95 dark:border-t-[#0a0f18]/90"></span></span></span>. 

Keiko liderava em nove das <span class="group relative inline cursor-pointer border-b-2 border-red-500/60 dark:border-red-500/40 hover:border-red-600 dark:hover:border-red-400 pb-0.5 font-semibold text-red-600 dark:text-red-500 transition-colors">11 capitais em que os peruanos puderam votar no País<!-- Tooltip --><span class="pointer-events-none absolute bottom-full left-1/2 -translate-x-1/2 mb-3 w-80 p-4 bg-zinc-950/95 dark:bg-[#0a0f18]/90 border border-red-500/30 dark:border-white/10 backdrop-blur-md rounded-xl text-xs text-stone-300 font-jakarta leading-relaxed shadow-2xl opacity-0 translate-y-2 group-hover:opacity-100 group-hover:translate-y-0 transition-all duration-300 z-50 normal-case not-italic text-left font-sans">Filtro Estatístico Asséptico: A tática da Esquerda Neototalitária aqui é focar excessivamente na contagem de cidades e números frios. O Progressismo Autoritário não quer que o leitor perceba que o cidadão trabalhador no exterior vota contra a esquerda de forma sistemática.<span class="absolute top-full left-1/2 -translate-x-1/2 border-8 border-transparent border-t-zinc-950/95 dark:border-t-[#0a0f18]/90"></span></span></span>: Belo Horizonte, Brasília, Curitiba, Goiânia, Manaus, Rio Branco, Rio de Janeiro, Salvador e São Paulo."'''

html = re.sub(
    r'"Segundo a deputada federal Coronel Fernanda.*?<div\s+class="flex items-center space-x-3',
    leitura_raio_x + '\n                                <!-- EXPOSIÇÃO DA AUTORIA -->\n                                <div\n                                    class="flex items-center space-x-3',
    html,
    flags=re.DOTALL
)

# 8. Exposição da Autoria
html = html.replace('O Globo Brasil', 'CartaCapital')

# 9. Artigo Técnico Detalhado
artigo = '''<p>
    Ao analisar o modo como a grande mídia retrata as disputas políticas na América do Sul, torna-se evidente que a <strong>Esquerda Neototalitária</strong> domina não apenas o que é dito, mas principalmente o que é omitido. A recente matéria da CartaCapital sobre as eleições presidenciais no Peru revela uma tática recorrente de <strong>Engenharia Social Coercitiva</strong>: o uso de estatísticas frias para anestesiar uma verdade inconveniente sobre a rejeição ao seu próprio projeto.
</p>
<p>
    O artigo foca obsessivamente na disputa voto a voto, celebrando uma leve vantagem geral da esquerda, mas trata o voto dos expatriados no Brasil como uma mera anedota geográfica. A realidade, porém, é cristalina: cidadãos que fogem do ciclo de instabilidade econômica e hiperinflação gerado por políticas progressistas na América Latina tornam-se, invariavelmente, eleitores da direita. O exílio é um sintoma, não um detalhe.
</p>
<p>
    O <strong>Progressismo Autoritário</strong> precisa, a todo custo, impedir que o leitor conecte os pontos. Para eles, admitir que 55% dos peruanos vivendo no Brasil rejeitam a esquerda seria admitir o fracasso de seu modelo social e econômico. A narrativa hegemônica prefere focar em rótulos do passado ("filha do ex-ditador") para deslegitimar a escolha de milhares de trabalhadores que buscam apenas estabilidade.
</p>
<p>
    Esta tática do <strong>Filtro Estatístico Asséptico</strong> é letal porque passa despercebida pela maioria. Ela encobre a falência moral de um modelo que força seus cidadãos a migrarem, tentando vender uma "vitória" apertada como uma escolha popular livre de consequências. A direita precisa acordar e entender que, na guerra de narrativas, expor a realidade por trás dos números é a nossa maior arma.
</p>'''

html = re.sub(
    r'<h3\s+class="font-playfair text-2xl md:text-3xl font-bold tracking-tight text-zinc-900 dark:text-white">\s*A Armadilha do Cavalo de Troia: O PL 1811/2026 e a Divisão da Base Conservadora\s*</h3>\s*<div\s+class="space-y-6 text-zinc-700 dark:text-stone-300/90 text-base md:text-lg leading-relaxed font-light font-jakarta">.*?</div>',
    '<h3 class="font-playfair text-2xl md:text-3xl font-bold tracking-tight text-zinc-900 dark:text-white">\n                                        A Fuga do Laboratório Socialista e a Engenharia dos Números\n                                    </h3>\n\n                                    <div\n                                        class="space-y-6 text-zinc-700 dark:text-stone-300/90 text-base md:text-lg leading-relaxed font-light font-jakarta">\n                                        ' + artigo + '\n                                    </div>',
    html,
    flags=re.DOTALL
)

# 10. Autópsia da Narrativa Box
manual_defesa_narrativa = "A mídia celebra a liderança esquerdista no Peru, mas esconde por que a maioria dos peruanos que fugiram pro Brasil votaram contra eles. Quem foge do laboratório socialista na América Latina nunca vota no Progressismo Autoritário, vota na direita para sobreviver. Usar números para esconder esse pânico é pura Engenharia Social Coercitiva."

html = re.sub(
    r'x-data="\{ copied: false, textToCopy: \'Pintar tornozeleiras de rosa.*?\n',
    f'x-data="{{ copied: false, textToCopy: \'{manual_defesa_narrativa}\' }}">\n',
    html
)
html = re.sub(
    r'A pauta utiliza a retórica da \'proteção\' para introduzir o\s*punitivismo seletivo e a desmoralização estética do acusado.*?armadilha montada pela militância\.',
    'A mídia utiliza a tática do "Filtro Estatístico Asséptico". Ao reduzir o voto dos expatriados a um placar de números, tentam anestesiar a realidade: o cidadão que foge das instabilidades nunca vota na esquerda.',
    html,
    flags=re.DOTALL
)
html = html.replace('Agenda de Desmoralização Masculina', 'Ocultação de Rejeição Popular')
html = re.sub(
    r'https://oglobo.globo.com/.*?.ghtml',
    'https://www.cartacapital.com.br/cartaexpressa/como-esta-a-disputa-entre-sanchez-e-keiko-fujimori-entre-peruanos-de-11-capitais-brasileiras/',
    html
)

# 11. Autópsia da Tática Box
manual_defesa_tatica = "Quando a Esquerda Neototalitária fala em números de votação no exterior, eles não querem que você perceba o essencial: o migrante é alguém que fugiu da miséria criada por eles mesmos. E quem foge do socialismo vota na direita."
html = re.sub(
    r'x-data="\{ copied: false, textToCopy: \'Pintar uma tornozeleira eletrônica de rosa não protege nenhuma mulher.*?\n',
    f'x-data="{{ copied: false, textToCopy: \'{manual_defesa_tatica}\' }}">\n',
    html
)
html = re.sub(
    r'O uso da sinalização estética e da espetacularização punitiva pelo\s*<strong>Progressismo Autoritário</strong> para disfarçar o afrouxamento real do\s*encarceramento provisório\.',
    'A utilização de dados estatísticos fragmentados pelo <strong>Progressismo Autoritário</strong> para camuflar a rejeição brutal ao seu projeto político entre os que vivem a realidade do exílio econômico.',
    html
)
html = re.sub(
    r'Desviar o foco da falência operacional do rastreamento eletrônico e incentivar\s*medidas cautelares alternativas, erodindo a severidade penal sob a premissa de\s*humilhação moral\.',
    'Blindar a narrativa de sucesso da esquerda na América Latina, evitando que a fuga massiva de cérebros e trabalhadores seja diretamente conectada ao fracasso do modelo socialista.',
    html
)

# 12. Dossiê Cavalo de Troia (Remover ou adaptar) -> Vou adaptar para a análise
html = html.replace('Dossiê Cavalo de Troia', 'Alerta de Engenharia')
html = html.replace('8.5 / 10', '9.0 / 10')
html = html.replace('width: 85%', 'width: 90%')

html = re.sub(
    r'A proposta, mesmo se apresentada sob legítima intenção protetiva.*?máquina progressista\.',
    'A linguagem asséptica atua como uma barreira cognitiva. O leitor desatento processa a informação como um mero dado geográfico, falhando em compreender o fenômeno profundo do colapso econômico que obriga a população a fugir e rejeitar as velhas lideranças.',
    html,
    flags=re.DOTALL
)
html = re.sub(
    r'Punitivismo seletivo de gênero, desmoralização da presunção de inocência e\s*introdução da agenda de espetacularização humilhante no código penal\.',
    'Omissão de causa e consequência. Ocultação do colapso econômico de países vizinhos para preservar a viabilidade eleitoral do mesmo modelo no Brasil.',
    html
)
html = re.sub(
    r'🚨 Manobra Eleitoral e Ideológica\. O projeto visa cindir o eleitorado e a base\s*do partido em ano de eleição, utilizando performáticas punitivas para sabotar o\s*debate técnico de segurança\.',
    '🚨 Controle de Narrativa e Gaslighting Estatístico. A imprensa age como um braço de relações públicas da esquerda sul-americana, higienizando os sintomas do colapso.',
    html
)

# 13. Ficha Técnica
html = html.replace('O Globo (Legislativo)', 'CartaCapital (Internacional)')
html = html.replace('#RX-5678-ROSA', '#RX-9921-PERU')


with open("d:/direita_intelectual/analise-cartacapital-peru.html", "w", encoding="utf-8") as f:
    f.write(html)

print("HTML gerado com sucesso!")
