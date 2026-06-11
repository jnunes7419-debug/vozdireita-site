import re

def main():
    with open('D:\\direita_intelectual\\analise-geopolitica-israel-ira.html', 'r', encoding='utf-8') as f:
        geo_html = f.read()

    capa_img = 'assets/dark_horse_autopsia.png'
    tag = 'Cultura Pop'
    tempo = '6 min'
    titulo = 'Dark Horse: A Engenharia Social Contra o Cinema Conservador'
    subtitulo = 'A CartaCapital tenta desqualificar o filme sobre o atentado a Bolsonaro, mas expõe o cinismo de roteiristas que faturam milhões com o monopólio cultural.'

    manchete = '"Dark Horse. Um roteiro que parece confuso no começo. E que no final parece o começo" – CartaCapital'
    premissa = 'A redação tenta desqualificar a estrutura do filme conservador sob o verniz de uma crítica cinematográfica isenta, ocultando o fato de que seu articulista é uma peça-chave do oligopólio corporativo de narrativas.'

    autopsia_lista = """
                        <li><strong>O Vínculo e a Cegueira Deliberada:</strong> Marton Olympio, que assina a ironia contra o filme, não é um ativista independente. Ele é um "roteirista de estúdio" faturando alto para empacotar o "ativismo identitário" como produto comercial para corporações como Disney, Paramount e Rede Globo.</li>
                        <li><strong>A Hipocrisia da Violência Estética:</strong> O autor zomba da dramatização do atentado contra Jair Bolsonaro, chamando-a de "pastelão". No entanto, ele atua na super-espetacularização da miséria ao escrever roteiros hiperviolentos (ex: <i>Alemão 2</i>), enriquecendo com a barbárie que critica nos outros.</li>
                        <li><strong>Gaslighting Financeiro:</strong> O ataque ao financiamento paralelo do filme de direita é uma tática de despiste. Tentam ridicularizar os conservadores para esconder que a "resistência cultural" de esquerda é, na verdade, a maior engrenagem de monopólio subsidiado do Brasil.</li>
    """

    quote = '"Eles riem de um assassinato real enquanto faturam milhões escrevendo sobre o tráfico. Não é crítica, é defesa de mercado."'

    diagnostico = """
                    <p>
                        A resenha publicada pela CartaCapital não é jornalismo cultural, é o braço armado da <strong>Esquerda Neototalitária</strong> protegendo seu feudo de narrativas. A crítica a <i>Dark Horse</i> atua através da <strong>Engenharia Social Coercitiva</strong> disfarçada de sarcasmo intelectual: ao invés de debater a visão cinematográfica opositora, buscam destruir o valor social de quem ousa produzi-la.
                    </p>
                    <p>
                        O <strong>Progressismo Autoritário</strong> tenta <a href="analise-padrao.html" class="text-gold-500 hover:underline">monopolizar a estética</a> e a moral da cultura nacional, rindo de um assassinato tentado enquanto blinda seus próprios roteiros sanguinários feitos para a elite do streaming. O objetivo não é falar sobre roteiro; é interditar a direita no audiovisual, perpetuando o <a href="dossie-agencias.html" class="text-gold-500 hover:underline">monopólio subsidiado da verdade</a>.
                    </p>
    """

    manual = '"Acreditar que o \'ativismo\' dos roteiristas apoiados pela CartaCapital é pura resistência é pura ingenuidade. No fundo, a militância deles é apenas o produto de prateleira mais lucrativo vendido para a Disney e para a Globo. Não existe superioridade moral quando você se esconde no monopólio para lucrar espetacularizando a violência que jura combater."'

    link = 'https://www.cartacapital.com.br/politica/dark-horse-um-roteiro-que-parece-confuso-no-comeco-e-que-no-final-parece-o-comeco/'
    fonte_nome = 'Veja a matéria no viés neototalitário na Carta Capital'

    # Pegamos o Geopolítica e trocamos os dados
    new_html = geo_html

    # Replace Title tag
    new_html = re.sub(r'<title>.*?</title>', '<title>Autópsia: CartaCapital e Dark Horse | Voz Direita</title>', new_html)
    new_html = re.sub(r'<meta name="description".*?>', '<meta name="description" content="Análise tática sobre como a mídia utiliza roteiristas do oligopólio para rebaixar produções de direita e monopolizar a cultura.">', new_html)

    # Replace Hero
    new_html = new_html.replace('geopolitica_israel_ira.png', capa_img)
    # Tem object-top já lá?
    new_html = new_html.replace('class="w-full h-full object-cover opacity-60', 'class="w-full h-full object-cover object-top opacity-60')
    
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
    new_html = re.sub(r'href="https://g1.*?ghtml"', f'href="{link}" target="_blank" rel="noopener"', new_html, count=1)
    new_html = re.sub(r'Ler Matéria Original no G1', fonte_nome, new_html, count=1)

    # Salva
    with open('D:\\direita_intelectual\\analise-cartacapital-darkhorse.html', 'w', encoding='utf-8') as f:
        f.write(new_html)

if __name__ == "__main__":
    main()
