import re

def main():
    with open('D:\\direita_intelectual\\analise-geopolitica-israel-ira.html', 'r', encoding='utf-8') as f:
        geo_html = f.read()

    # O texto do CartaCapital
    capa_img = 'assets/grafico_pesquisa_es_1781048521496.png'
    tag = 'Análise de Mídia'
    tempo = '5 min'
    titulo = 'O Falso Empate: A Engenharia Social nas Pesquisas'
    subtitulo = 'Como a Esquerda Neototalitária usa manchetes para mascarar a liderança real da oposição e criar uma ilusão de estabilidade para o regime.'

    manchete = '"A disputa entre Lula e Flávio Bolsonaro no Espírito Santo, segundo o Real Time Big Data"'
    premissa = 'O texto foca estrategicamente no cenário de primeiro turno (35% a 34%) como um mero "empate técnico", mas oculta da chamada principal a vitória consolidada da oposição no segundo turno (48% a 43%).'

    autopsia_lista = """
                        <li><strong>A manipulação semântica do "empate":</strong> A manchete enfatiza a indefinição temporária do primeiro turno para atenuar o avanço e a liderança além da margem de erro da direita no cenário decisivo.</li>
                        <li><strong>A blindagem do desgaste governista:</strong> A reportagem age como contenção de danos ao não admitir que o presidente, possuindo a máquina federal, é incapaz de superar a oposição em um estado estratégico.</li>
                        <li><strong>Isolamento de dados desfavoráveis:</strong> O veículo dilui a derrota governista no meio do texto, dificultando a leitura rápida e impedindo a formação do "efeito manada" favorável à oposição.</li>
    """

    quote = '"A supressão do horizonte no segundo turno não é um erro de edição, é uma arma de controle da percepção."'

    diagnostico = """
                    <p>
                        A estrutura desta manchete é um exemplo clássico da operação da <strong>Esquerda Neototalitária</strong> para modelar a percepção da realidade. A tática aqui é o enquadramento de supressão (framing): ao destacar a indefinição do primeiro turno e suprimir do título o revés contundente do governo no segundo, exerce-se a <strong>Engenharia Social Coercitiva</strong>.
                    </p>
                    <p>
                        O leitor é forçado a absorver uma falsa sensação de estabilidade que os próprios dados da matéria desmentem cabalmente. É a instrumentalização fria dos números a serviço do <strong>Progressismo Autoritário</strong>, reembalando a rejeição popular para desmotivar a base conservadora.
                    </p>
    """

    manual = '"A mídia insiste em vender a narrativa do \'empate técnico\', mas a própria pesquisa que eles citam confirma a liderança com vantagem real da oposição no segundo turno. Isso não é um erro da redação, mas sim o Neototalitarismo midiático em ação: esconder o declínio e a rejeição de um governo falido para tentar anestesiar o eleitor através do controle da manchete."'

    link = 'https://www.cartacapital.com.br/politica/a-disputa-entre-lula-e-flavio-bolsonaro-no-espirito-santo-segundo-o-real-time-big-data/'
    fonte_nome = 'CartaCapital'

    # Pegamos o Geopolítica e trocamos os dados
    new_html = geo_html

    # Replace Title tag
    new_html = re.sub(r'<title>.*?</title>', '<title>Autópsia: A Manipulação do Empate Técnico | Voz Direita</title>', new_html)
    new_html = re.sub(r'<meta name="description".*?>', '<meta name="description" content="Análise tática sobre como a grande mídia utiliza o enquadramento de supressão para mascarar as vitórias da direita no segundo turno das pesquisas eleitorais.">', new_html)

    # Replace Hero
    new_html = new_html.replace('geopolitica_israel_ira.png', capa_img)
    new_html = new_html.replace('Geopolítica Global', tag)
    new_html = new_html.replace('A Inversão de Culpabilidade: O Eixo Irã-Israel', titulo)
    new_html = new_html.replace('Como a Hegemonia do Jornalismo manipula a linha do tempo do conflito para transformar agressores contumazes em vítimas e nações soberanas em vilões.', subtitulo)

    # 1. MANCHETE
    new_html = re.sub(r'<div class="p-6 bg-zinc-100.*?</div>', f'<div class="p-6 bg-zinc-100 dark:bg-zinc-900/50 rounded-lg border border-zinc-200 dark:border-zinc-800 mb-8 italic">\n                        {manchete}\n                    </div>', new_html, count=1, flags=re.DOTALL)
    new_html = re.sub(r'<strong>A Falsa Premissa:</strong>.*?</p>', f'<strong>A Falsa Premissa:</strong> {premissa}\n                    </p>', new_html, count=1, flags=re.DOTALL)

    # 2. AUTÓPSIA
    new_html = re.sub(r'<ul class="space-y-4 list-disc list-inside">.*?</ul>', f'<ul class="space-y-4 list-disc list-inside">\n{autopsia_lista}                    </ul>', new_html, count=1, flags=re.DOTALL)

    # QUOTE
    new_html = re.sub(r'<p class="font-playfair text-2xl md:text-3xl font-medium text-zinc-900 dark:text-gold-400 italic mb-0 leading-tight">.*?</p>', f'<p class="font-playfair text-2xl md:text-3xl font-medium text-zinc-900 dark:text-gold-400 italic mb-0 leading-tight">\n                        {quote}\n                    </p>', new_html, count=1, flags=re.DOTALL)

    # 3. DIAGNÓSTICO
    new_html = re.sub(r'<h3 class="font-playfair text-3xl font-bold text-zinc-900 dark:text-white mb-6 border-l-4 border-gold-500 pl-4">\s*3\. O DIAGNÓSTICO DA TÁTICA \(A Ação Neototalitária\)\s*</h3>\s*<p>.*?</p>\s*<p>.*?</p>', f'<h3 class="font-playfair text-3xl font-bold text-zinc-900 dark:text-white mb-6 border-l-4 border-gold-500 pl-4">\n                        3. O DIAGNÓSTICO DA TÁTICA (A Ação Neototalitária)\n                    </h3>\n{diagnostico}', new_html, count=1, flags=re.DOTALL)

    # 4. MANUAL
    new_html = re.sub(r'"A grande mídia usa a tática de inversão de culpa.*?"', manual, new_html, count=1, flags=re.DOTALL)
    
    # FONTE
    new_html = re.sub(r'href="https://g1.*?ghtml"', f'href="{link}"', new_html, count=1)
    new_html = re.sub(r'Ler Matéria Original no G1', f'Ler Matéria Original na {fonte_nome}', new_html, count=1)

    # A imagem da capa no topo
    new_html = new_html.replace('assets/assets/grafico_pesquisa_es_1781048521496.png', capa_img)

    with open('D:\\direita_intelectual\\analise-carta-capital-pesquisa.html', 'w', encoding='utf-8') as f:
        f.write(new_html)

if __name__ == "__main__":
    main()
