import re

def create_article():
    template_path = 'd:\\direita_intelectual\\modelo-post.html'
    output_path = 'd:\\direita_intelectual\\analise-g1-ype.html'
    
    with open(template_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Replacements
    # 1. Background image
    html = re.sub(r'assets/guerra_pop_1\.png', 'assets/sabotagem_ype.png', html)
    
    # 2. Top Tag
    html = re.sub(r'Guerra Cultural', 'Aparelhamento Burocrático', html)
    
    # 3. Main Title
    html = re.sub(r'<h1 class="font-playfair text-5xl[^>]*>.*?</h1>', '<h1 class="font-playfair text-5xl md:text-7xl lg:text-8xl font-bold tracking-tight text-white leading-[1.1] mb-6 drop-shadow-2xl max-w-4xl">\n                O Terror Burocrático: O Caso Ypê\n            </h1>', html, flags=re.DOTALL)
    
    # 4. Description
    html = re.sub(r'<p class="text-lg md:text-2xl text-zinc-300 font-light max-w-2xl leading-relaxed">.*?</p>', '<p class="text-lg md:text-2xl text-zinc-300 font-light max-w-2xl leading-relaxed">\n                A esquerda neototalitária instrumentaliza a Anvisa para impor a engenharia social coercitiva sobre a indústria nacional.\n            </p>', html, flags=re.DOTALL)
    
    # 5. Content Body
    demolidor_content = """
                    <!-- O CONTEÚDO DO ARTIGO -->
                    <div class="prose prose-lg prose-zinc dark:prose-invert max-w-none font-jakarta">

                        <h2 class="text-gold-600 dark:text-gold-500 font-playfair font-bold mt-12 mb-6">
                            1. A MANCHETE OFICIAL (A Isca)
                        </h2>
                        <blockquote class="border-l-4 border-gold-500 pl-6 my-8 italic text-zinc-700 dark:text-zinc-300 bg-white/50 dark:bg-zinc-900/50 p-6 rounded-r-lg shadow-sm">
                            <p class="font-bold text-xl mb-2 text-zinc-900 dark:text-white">"Ypê: final 1 no lote identifica produtos feitos em Amparo, onde duas fábricas seguem paradas"</p>
                            <p class="text-base text-zinc-500 dark:text-zinc-400 mt-2">— A Falsa Premissa: Um mero rigor sanitário técnico e neutro da Anvisa visando a proteção exclusiva da saúde pública.</p>
                        </blockquote>

                        <h2 class="text-gold-600 dark:text-gold-500 font-playfair font-bold mt-12 mb-6">
                            2. A AUTÓPSIA DO FATO (A Realidade Oculta)
                        </h2>
                        <ul class="space-y-4 mb-8">
                            <li class="flex items-start">
                                <span class="text-gold-500 mr-3 text-xl font-bold">•</span>
                                <span><strong>A Punição Financeira:</strong> A narrativa estatal omite intencionalmente que a família Beira, proprietária da Ypê, doou R$ 1,5 milhão como pessoa física para a campanha de Jair Bolsonaro em 2022. Esta é a verdadeira "contaminação" que o sistema quer extirpar.</span>
                            </li>
                            <li class="flex items-start">
                                <span class="text-gold-500 mr-3 text-xl font-bold">•</span>
                                <span><strong>Histeria Microbiológica:</strong> Utilizam jargões técnicos alarmistas ("Pseudomonas aeruginosa") para gerar pânico e destruir a reputação de uma empresa nacional, ignorando que os lotes já haviam sido retidos pelo rigoroso controle de qualidade interno da própria fábrica.</span>
                            </li>
                            <li class="flex items-start">
                                <span class="text-gold-500 mr-3 text-xl font-bold">•</span>
                                <span><strong>A Agência como Braço Armado:</strong> A paralisação do complexo de Amparo (que concentra a maior parte do catálogo de 450 produtos) não é precaução de saúde; é uma retaliação calculada e um aviso claro ao empresariado brasileiro que ousar financiar a oposição política.</span>
                            </li>
                        </ul>

                        <h2 class="text-gold-600 dark:text-gold-500 font-playfair font-bold mt-12 mb-6">
                            3. O DIAGNÓSTICO DA TÁTICA (A Ação Neototalitária)
                        </h2>
                        <p class="mb-6 leading-relaxed">
                            A <strong>Esquerda Neototalitária</strong> instrumentaliza agências reguladoras (como a Anvisa) para operarem como verdadeiras milícias burocráticas. Sob o escudo irrefutável e covarde da "proteção sanitária", eles aplicam a <strong>Engenharia Social Coercitiva</strong> para perseguir e sangrar adversários ideológicos. Quando o judiciário trabalhista falha em intimidar (como tentaram com a acusação de "assédio eleitoral"), acionam a vigilância sanitária. O objetivo não é limpar detergentes, é sujar biografias e estipular o terror burocrático: qualquer empresário que não se ajoelhar ao <strong>Progressismo Autoritário</strong> terá suas fábricas lacradas pelo peso do Estado.
                        </p>

                        <div class="my-12 p-8 bg-gradient-to-br from-zinc-100 to-white dark:from-intel-900 dark:to-zinc-900 border border-zinc-200 dark:border-white/10 rounded-2xl shadow-xl relative overflow-hidden">
                            <div class="absolute top-0 right-0 w-32 h-32 bg-gold-500/10 rounded-full blur-3xl"></div>
                            
                            <h2 class="text-gold-600 dark:text-gold-500 font-playfair font-bold mb-6 flex items-center">
                                <svg class="w-6 h-6 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"></path></svg>
                                4. O MANUAL DE DEFESA (Arma Intelectual)
                            </h2>
                            <p class="text-xl md:text-2xl font-playfair italic text-zinc-800 dark:text-zinc-200 leading-relaxed mb-6">
                                "A Anvisa paralisar a Ypê logo após a empresa ter doado R$ 1,5 milhão a Bolsonaro em 2022 não é coincidência, é retaliação. A Esquerda Neototalitária usa o Estado não para proteger sua saúde, mas para quebrar financeiramente quem apoia a oposição. O nome disso é perseguição política."
                            </p>
                            <button class="flex items-center space-x-2 text-xs font-bold uppercase tracking-widest text-white bg-gold-600 hover:bg-gold-500 px-6 py-3 rounded-lg transition-all shadow-lg hover:shadow-gold-500/25" onclick="navigator.clipboard.writeText('A Anvisa paralisar a Ypê logo após a empresa ter doado R$ 1,5 milhão a Bolsonaro em 2022 não é coincidência, é retaliação. A Esquerda Neototalitária usa o Estado não para proteger sua saúde, mas para quebrar financeiramente quem apoia a oposição. O nome disso é perseguição política.')">
                                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z"></path></svg>
                                <span>Copiar para WhatsApp</span>
                            </button>
                        </div>
                    </div>
"""
    # Replace content between <article... and </article>
    # Find the article section using regex
    start_article = r'<!-- ARTIGO PRINCIPAL -->'
    end_article = r'</article>'
    
    match_start = re.search(start_article, html)
    match_end = re.search(end_article, html)
    
    if match_start and match_end:
        html = html[:match_start.start()] + demolidor_content + "\n                </article>" + html[match_end.end():]
        
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
        
if __name__ == '__main__':
    create_article()
