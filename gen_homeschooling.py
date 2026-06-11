import re

with open('analise-g1-homeschooling.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace metadata
content = content.replace(
    'Autópsia: A Simetria do Privilégio e o Progressismo Autoritário | Voz Direita',
    'Autópsia: A Criminalização da Educação e o Neototalitarismo | Voz Direita'
)
content = content.replace(
    'Autópsia forense da soltura de Monique Medeiros. Entenda como o progressismo autoritário e a engenharia social coercitiva atuam para naturalizar a impunidade na segurança pública.',
    'Autópsia forense da condenação de pais em Jales (SP). Entenda como a criminalização do homeschooling é a face mais agressiva da engenharia social coercitiva.'
)
content = content.replace(
    'Voz Direita, Monique Medeiros, Henry Borel, G1, Globo, Engenharia Social Coercitiva, Esquerda Neototalitária, Progressismo Autoritário, Neototalitarismo, Jander Nunes, Segurança Pública',
    'Voz Direita, Homeschooling, Ensino Domiciliar, Jales, G1, Globo, Engenharia Social Coercitiva, Esquerda Neototalitária, Progressismo Autoritário, Neototalitarismo, Jander Nunes'
)

# Replace Hero
content = content.replace('ALVO: G1 RIO DE JANEIRO', 'ALVO: G1 RIO PRETO')
content = content.replace(
    'A Simetria do Privilégio: <br class="hidden md:inline"><span class="text-transparent bg-clip-text bg-gradient-to-r from-red-600 to-gold-400">Como o Progressismo Autoritário Naturaliza a Impunidade</span>',
    'A Criminalização do Cuidado: <br class="hidden md:inline"><span class="text-transparent bg-clip-text bg-gradient-to-r from-red-600 to-gold-400">O Estado Contra as Famílias e o Homeschooling</span>'
)
content = content.replace(
    'Uma autópsia forense da soltura de Monique Medeiros e do silêncio ético da grande mídia consorciada.',
    'Uma autópsia forense da condenação judicial por ensino domiciliar e a imposição do neototalitarismo escolar.'
)
content = content.replace('06 de Junho, 2026', '28 de Abril, 2026')

# Replace Image and News Block
content = content.replace('assets/monique_liberada.png', 'assets/homeschooling_condenacao.png')
content = content.replace('05/04/2022', '28/04/2026')
content = content.replace(
    '"Decisão libera Monique Medeiros, mãe de Henry, da prisão com tornozeleira eletrônica"',
    '"Pais são condenados por deixarem de levar filhas à escola no interior de SP"'
)
content = content.replace(
    'Falsa Premissa: A imprensa hegemônica busca naturalizar a concessão de liberdade domiciliar monitorada para uma ré de crime hediondo, tratando as deficiências de ordem dos presídios como justificativa moral válida.',
    'Falsa Premissa: A manchete e o Estado rotulam como "abandono intelectual" uma escolha deliberada e estruturada de ensino domiciliar (homeschooling), criminalizando pais zelosos como se fossem negligentes.'
)

# Replace Raio-X box
raio_x = '''<p class="font-playfair text-lg md:text-xl text-zinc-800 dark:text-stone-200 leading-loose italic max-w-4xl font-light">
                            "Os pais de duas meninas foram condenados por deixarem de levar as filhas à escola em Jales (SP)... A decisão estabeleceu a pena de 50 dias de detenção em regime inicial semiaberto. Segundo o processo, os pais 
                            <span class="group relative inline cursor-pointer border-b-2 border-red-500/60 dark:border-red-500/40 hover:border-red-600 dark:hover:border-red-400 pb-0.5 font-semibold text-red-600 dark:text-red-500 transition-colors">
                                deixaram de levar as filhas à escola
                                <!-- Tooltip -->
                                <span class="pointer-events-none absolute bottom-full left-1/2 -translate-x-1/2 mb-3 w-80 p-4 bg-zinc-950/95 dark:bg-[#0a0f18]/90 border border-red-500/30 dark:border-white/10 backdrop-blur-md rounded-xl text-xs text-stone-300 font-jakarta leading-relaxed shadow-2xl opacity-0 translate-y-2 group-hover:opacity-100 group-hover:translate-y-0 transition-all duration-300 z-50 normal-case not-italic text-left font-sans">
                                    Omissão da Qualidade Educacional: A matéria omite no título e trata como crime o fato de as crianças estarem recebendo aulas estruturadas em casa ministradas por dois professores particulares pagos pela família.
                                    <span class="absolute top-full left-1/2 -translate-x-1/2 border-8 border-transparent border-t-zinc-950/95 dark:border-t-[#0a0f18]/90"></span>
                                </span>
                            </span> 
                            desde o ensino fundamental. O juiz pontuou que a legislação determina que os pais são obrigados a submeter seus filhos ao ensino na forma regulamentada, sob pena de 
                            <span class="group relative inline cursor-pointer border-b-2 border-red-500/60 dark:border-red-500/40 hover:border-red-600 dark:hover:border-red-400 pb-0.5 font-semibold text-red-600 dark:text-red-500 transition-colors">
                                abandono intelectual
                                <!-- Tooltip -->
                                <span class="pointer-events-none absolute bottom-full left-1/2 -translate-x-1/2 mb-3 w-80 p-4 bg-zinc-950/95 dark:bg-[#0a0f18]/90 border border-red-500/30 dark:border-white/10 backdrop-blur-md rounded-xl text-xs text-stone-300 font-jakarta leading-relaxed shadow-2xl opacity-0 translate-y-2 group-hover:opacity-100 group-hover:translate-y-0 transition-all duration-300 z-50 normal-case not-italic text-left font-sans">
                                    Engenharia Social Coercitiva: A Esquerda Neototalitária muda o significado das palavras, chamando de 'abandono' o investimento rigoroso dos pais na educação dos próprios filhos.
                                    <span class="absolute top-full left-1/2 -translate-x-1/2 border-8 border-transparent border-t-zinc-950/95 dark:border-t-[#0a0f18]/90"></span>
                                </span>
                            </span> 
                            ... A mãe alegou ter agido para contribuir para o reconhecimento do ensino domiciliar, tese rejeitada pelo magistrado."
                        </p>'''

content = re.sub(
    r'<p class="font-playfair text-lg md:text-xl.*?</p>',
    raio_x,
    content,
    flags=re.DOTALL
)

# Replace target
content = content.replace(
    'ALVO DA AUTÓPSIA: Cobertura factual e reprodução de despacho jurídico pelo portal \n                        <span class="text-zinc-900 dark:text-white font-bold underline decoration-red-600 decoration-2 underline-offset-4 tracking-wide hover:text-red-600 dark:hover:text-red-400 transition-colors">G1 Rio de Janeiro</span> \n                        - 05/04/2022.',
    'ALVO DA AUTÓPSIA: Cobertura factual e reprodução de despacho jurídico pelo portal \n                        <span class="text-zinc-900 dark:text-white font-bold underline decoration-red-600 decoration-2 underline-offset-4 tracking-wide hover:text-red-600 dark:hover:text-red-400 transition-colors">G1 Rio Preto e Araçatuba</span> \n                        - 28/04/2026.'
)

# Replace the article content
article_html = '''<h3 class="font-playfair text-2xl md:text-3xl font-bold tracking-tight text-zinc-900 dark:text-white">
                        A Criminalização da Educação: Como o Estado Esmaga a Família
                    </h3>
                    
                    <div class="space-y-6 text-zinc-700 dark:text-stone-300/90 text-sm md:text-base leading-relaxed font-light font-jakarta">
                        <p>
                            A desintegração moral de uma nação consolida-se quando suas instituições passam a tratar o instinto de proteção parental não como virtude, mas como ameaça. O recente caso em que pais foram condenados em Jales, no interior de São Paulo, à pena de detenção e serviços comunitários simplesmente por optarem por educar suas filhas em casa, revela o estágio avançado do <strong>Neototalitarismo</strong> em solo brasileiro. Trata-se de uma aplicação flagrante e brutal da <strong>Engenharia Social Coercitiva</strong>: o aparelho estatal apropria-se do monopólio da educação e da moralidade, forçando famílias a se submeterem às engrenagens do sistema institucionalizado sob pena de prisão.
                        </p>
                        
                        <p>
                            A narrativa imposta pela grande mídia e chancelada por sentenças judiciais descreve essa escolha consciente e estruturada como "abandono intelectual". Essa alteração proposital no significado das palavras não é acidental, é uma tática central da <strong>Esquerda Neototalitária</strong>. Ao rotular o ensino domiciliar como um delito análogo à negligência, o Estado higieniza sua própria violência, escondendo que as crianças não estavam desamparadas, mas sim recebendo aulas estruturadas ministradas pela mãe e por dois professores particulares contratados pela família. A intenção não é proteger a inteligência dos menores, mas sim punir a autonomia dos responsáveis.
                        </p>

                        <p>
                            Observa-se aqui a mais pura hipocrisia do <strong>Progressismo Autoritário</strong>. O mesmo sistema jurídico e social que demonstra complacência e garantismo com réus de crimes hediondos, soltando diariamente traficantes, homicidas e lideranças de facções criminosas através de malabarismos de "medidas cautelares alternativas", não hesita em mobilizar todo o peso de sua força punitiva contra pais que desejam apenas exercer o direito de educar seus filhos longe das doutrinações ideológicas institucionais. Enquanto a leniência e a "ressocialização" são oferecidas aos que destroem a sociedade de fora para dentro, o rigor absoluto é reservado aos cidadãos de bem que buscam preservar a integridade mental e moral de seus próprios lares.
                        </p>

                        <p>
                            A educação compulsória pelo Estado deixou de ser um instrumento civilizatório de erradicação do analfabetismo e tornou-se a ferramenta primordial para o controle comportamental da próxima geração. A escola não é mais tratada como um simples meio de acesso ao conhecimento, mas como um pedágio ideológico obrigatório e monopolista. Quando o juízo afirma expressamente que "os pais são obrigados a submeter seus filhos ao ensino na forma regulamentada", a mensagem implícita é assustadora: o conteúdo exato do que se ensina em casa importa muito menos do que a submissão incondicional à estrutura metodológica previamente validada pelo aparelho estatal.
                        </p>

                        <p>
                            A criminalização do <em>homeschooling</em> e a ameaça de prisão para chefes de família revelam que o verdadeiro crime cometido por estes pais, aos olhos do <em>establishment</em>, nunca foi o suposto "abandono". O crime irreparável foi a insubordinação. O crime foi a presunção intolerável de que eles, os pais, possuem primazia natural, biológica e espiritual sobre a formação moral de suas filhas em detrimento dos burocratas do Estado. A Esquerda Neototalitária compreende perfeitamente que, para exercer controle total sobre as opiniões políticas, a moral sexual e a visão de mundo das próximas décadas, é absolutamente imperativo destruir a soberania da família tradicional hoje.
                        </p>

                        <p>
                            Neste cenário, a grande imprensa atua não como observadora isenta, mas como cúmplice diligente e militante ativa dessa repressão. As manchetes omitem frequentemente a qualidade superior da instrução domiciliar oferecida e concentram-se morbidamente no punitivismo aplicado, servindo como uma peça de intimidação didática para qualquer outra família que também ouse questionar ou desafiar a matriz escolar padronizada. Há um esforço contínuo de Engenharia Social Coercitiva para fazer a opinião pública enxergar essas famílias pioneiras como extremistas perigosos, sectários e irresponsáveis, em vez de reconhecê-los como verdadeiros heróis na defesa das liberdades civis essenciais.
                        </p>

                        <p>
                            Se o amor incondicional de um pai e uma mãe, consubstanciado no extremo sacrifício de dedicar a própria vida a ensinar em casa, passa a ser tipificado criminalmente e classificado como motivo de detenção em regime semiaberto — tudo isso num país sufocado pela mais brutal criminalidade violenta da América Latina —, então os conceitos universais de justiça e tirania foram irrevogavelmente invertidos pelo sistema dominante.
                        </p>

                        <p>
                            A defesa irrestrita da liberdade de ensino e a regulamentação protetiva do <em>homeschooling</em> devem assumir a linha de frente de qualquer movimento autêntico que busque resistir ao aparelhamento cultural e à censura. Uma nação cujas leis e magistrados ameaçam encarcerar mães e pais sob o cínico pretexto do "bem-estar intelectual da criança" já perdeu o direito moral de invocar os valores do Estado de Direito e da Democracia. Somente a recusa implacável e diária em adotar a narrativa manipulada e o vocabulário adulterado da Esquerda Neototalitária pode frear o avanço predatório desse sequestro institucionalizado das nossas famílias e do nosso futuro.
                        </p>

                        <p class="pt-6 border-t border-zinc-200 dark:border-zinc-800 text-xs font-mono text-zinc-500">
                            Para fins de transparência documental e auditoria editorial, a notícia original que descreve os termos técnicos da condenação dos pais no interior de São Paulo pode ser acessada na íntegra através do portal de notícias <a href="https://g1.globo.com/sp/sao-jose-do-rio-preto-aracatuba/noticia/2026/04/28/pais-sao-condenados-por-deixarem-de-levar-filhas-a-escola-no-interior-de-sp.ghtml" target="_blank" rel="noopener noreferrer" class="text-red-500 hover:underline inline-flex items-center">G1 Globo &nbsp;🔗</a>.
                        </p>
                    </div>'''

content = re.sub(
    r'<h3 class="font-playfair text-2xl md:text-3xl font-bold tracking-tight text-zinc-900 dark:text-white">.*?</a>.\n                        </p>\n                    </div>',
    article_html,
    content,
    flags=re.DOTALL
)

# Sidebar updates
content = content.replace(
    '''textToCopy: 'A soltura de uma acusada de assassinar o próprio filho demonstra como o Neototalitarismo aparelhou a justiça para proteger criminosos e punir a sociedade. O pretexto humanitário é sempre seletivo: serve para mandar réus hediondos para casa e manter cidadãos comuns reféns do medo. Quem aceita a inversão moral da justiça abre mão do direito elementar de defender suas crianças e sua própria segurança.' }''',
    '''textToCopy: 'A condenação de pais que contratam professores particulares para educar seus filhos em casa, enquanto criminosos hediondos são libertados diariamente no Brasil, não é justiça, é perseguição de Estado. O Neototalitarismo não pune a falta de educação, ele pune as famílias que se recusam a entregar a mente de suas crianças ao monopólio da doutrinação institucional. Uma sociedade que ameaça prender pais zelosos sob a desculpa de "abandono intelectual" já perdeu o direito de falar em democracia ou liberdade.' }'''
)

content = content.replace(
    'A naturalização da impunidade de crimes hediondos por meio do <strong>Progressismo Autoritário</strong> e de termos jurídicos higienizados que desviam a atenção da atrocidade do fato.',
    'A criminalização do ensino domiciliar através da Engenharia Social Coercitiva, usando a falsa premissa do "abandono intelectual" para forçar a doutrinação estatal.'
)

content = content.replace(
    'Promover o desencarceramento sistemático e a indiferença moral na opinião pública, erodindo a firmeza punitiva do sistema de justiça criminal.',
    'Sequestrar a autoridade dos pais sobre as crianças, erradicando a autonomia moral das famílias e garantindo o monopólio ideológico da Esquerda Neototalitária sobre a próxima geração.'
)

content = content.replace('G1 Rio (Casos Penais)', 'G1 SP (Perseguição a Famílias)')
content = content.replace('#RX-8761-MONIQUE', '#RX-4026-HOMESCHOOLING')

with open('analise-g1-homeschooling.html', 'w', encoding='utf-8') as f:
    f.write(content)

