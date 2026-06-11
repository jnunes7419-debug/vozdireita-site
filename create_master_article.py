import re

def create_master_article():
    template_path = 'd:\\direita_intelectual\\modelo-post.html'
    output_path = 'd:\\direita_intelectual\\analise-g1-master.html'
    
    with open(template_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Replacements
    # 1. Background image (using generic dark background for now as per premium design)
    html = re.sub(r'assets/guerra_pop_1\.png', 'assets/newsroom_banner.png', html)
    
    # 2. Top Tag
    html = re.sub(r'Guerra Cultural', 'Aparelhamento Jurídico', html)
    
    # 3. Main Title
    html = re.sub(r'<h1 class="font-playfair text-5xl[^>]*>.*?</h1>', '<h1 class="font-playfair text-5xl md:text-7xl lg:text-8xl font-bold tracking-tight text-white leading-[1.1] mb-6 drop-shadow-2xl max-w-4xl">\n                A Justiça Seletiva e o Caso Master\n            </h1>', html, flags=re.DOTALL)
    
    # 4. Description
    html = re.sub(r'<h2 class="font-jakarta text-xl md:text-2xl text-zinc-300 font-light max-w-3xl leading-relaxed border-l-4 border-gold-500 pl-6 drop-shadow-lg">.*?</h2>', '<h2 class="font-jakarta text-xl md:text-2xl text-zinc-300 font-light max-w-3xl leading-relaxed border-l-4 border-gold-500 pl-6 drop-shadow-lg">\n                Como as manobras no judiciário e a rejeição de delações operam a proteção seletiva e a manutenção do ecossistema corporativo.\n            </h2>', html, flags=re.DOTALL)
    
    # 5. Content Body
    demolidor_content = """
                    <!-- O CONTEÚDO DO ARTIGO -->
                    <div class="prose prose-lg prose-zinc dark:prose-invert max-w-none font-jakarta">

                        <h2 class="text-gold-600 dark:text-gold-500 font-playfair font-bold mt-12 mb-6">
                            1. A MANCHETE OFICIAL (A Isca)
                        </h2>
                        <blockquote class="border-l-4 border-gold-500 pl-6 my-8 italic text-zinc-700 dark:text-zinc-300 bg-white/50 dark:bg-zinc-900/50 p-6 rounded-r-lg shadow-sm">
                            <p class="font-bold text-xl mb-2 text-zinc-900 dark:text-white">"Caso Master: PF rejeita segunda proposta de delação premiada de Daniel Vorcaro"</p>
                            <p class="text-base text-zinc-500 dark:text-zinc-400 mt-2">— A Falsa Premissa: A ideia de que as instituições operam com rigor imparcial, analisando friamente a validade jurídica de um acordo de colaboração.</p>
                        </blockquote>

                        <h2 class="text-gold-600 dark:text-gold-500 font-playfair font-bold mt-12 mb-6">
                            2. A AUTÓPSIA DO FATO (A Realidade Oculta)
                        </h2>
                        <ul class="space-y-4 mb-8">
                            <li class="flex items-start">
                                <span class="text-gold-500 mr-3 text-xl font-bold">•</span>
                                <span><strong>Proteção em Cadeia:</strong> A PF afirma que o acordo foi rejeitado porque Vorcaro "agia para proteger pessoas próximas". Na verdade, a rejeição do acordo muitas vezes mascara a negociação submersa sobre *quem* o sistema permite que seja delatado e quem possui a blindagem institucional.</span>
                            </li>
                            <li class="flex items-start">
                                <span class="text-gold-500 mr-3 text-xl font-bold">•</span>
                                <span><strong>A Ampliação de Escopo Estratégica:</strong> O texto diz que a perícia inicial nos celulares "já revelou que o esquema [...] envolve corrupção, organização criminosa e uso de milícia privada para atacar adversários". É o clássico "fishing expedition": utiliza-se a investigação financeira como pretexto para uma devassa política, abrindo margem para criminalizar alvos periféricos conforme a conveniência de momento.</span>
                            </li>
                            <li class="flex items-start">
                                <span class="text-gold-500 mr-3 text-xl font-bold">•</span>
                                <span><strong>O Paralelismo Simbólico:</strong> Fazer questão de citar que a sala onde Vorcaro esteve ("sala de Estado-maior") é "o mesmo espaço usado para prender o ex-presidente Jair Bolsonaro". É a tentativa rasteira de criar uma associação mental inconsciente no leitor entre fraudes bilionárias e o líder da oposição conservadora, que não tem qualquer relação com o Caso Master.</span>
                            </li>
                        </ul>

                        <h2 class="text-gold-600 dark:text-gold-500 font-playfair font-bold mt-12 mb-6">
                            3. O DIAGNÓSTICO DA TÁTICA (A Ação Neototalitária)
                        </h2>
                        <p class="mb-6 leading-relaxed">
                            Estamos diante da manipulação clássica do jornalismo investigativo a serviço do <strong>Progressismo Autoritário</strong>. A imprensa reporta o fato (a rejeição da delação) mas enxerta no texto associações sutis de imagem e caráter. Quando a redação do G1 faz questão de atar a imagem do banqueiro preso às instalações utilizadas por Jair Bolsonaro, não estão informando: estão exercendo <strong>Engenharia Social Coercitiva</strong>. É a tática de 'contaminação por proximidade geográfica'. Enquanto a oposição é sempre associada ao crime, o verdadeiro aparelhamento das instituições, que escolhem seletivamente que delações aceitar e que esquemas proteger, segue oculto nas entrelinhas.
                        </p>

                        <div class="my-12 p-8 bg-gradient-to-br from-zinc-100 to-white dark:from-intel-900 dark:to-zinc-900 border border-zinc-200 dark:border-white/10 rounded-2xl shadow-xl relative overflow-hidden">
                            <div class="absolute top-0 right-0 w-32 h-32 bg-gold-500/10 rounded-full blur-3xl"></div>
                            
                            <h2 class="text-gold-600 dark:text-gold-500 font-playfair font-bold mb-6 flex items-center">
                                <svg class="w-6 h-6 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"></path></svg>
                                4. O MANUAL DE DEFESA (Arma Intelectual)
                            </h2>
                            <p class="text-xl md:text-2xl font-playfair italic text-zinc-800 dark:text-zinc-200 leading-relaxed mb-6">
                                "É vergonhoso como a mídia usa uma notícia sobre fraudes bancárias bilionárias (Caso Master) só para tentar sujar a imagem de Bolsonaro citando a cela em que ele ficou. O sistema escolhe a dedo quais delações aceitar para proteger seus próprios aliados, enquanto a Esquerda Neototalitária tenta, de forma patética, ligar a corrupção aos seus inimigos políticos."
                            </p>
                            <button class="flex items-center space-x-2 text-xs font-bold uppercase tracking-widest text-white bg-gold-600 hover:bg-gold-500 px-6 py-3 rounded-lg transition-all shadow-lg hover:shadow-gold-500/25" onclick="navigator.clipboard.writeText('É vergonhoso como a mídia usa uma notícia sobre fraudes bancárias bilionárias (Caso Master) só para tentar sujar a imagem de Bolsonaro citando a cela em que ele ficou. O sistema escolhe a dedo quais delações aceitar para proteger seus próprios aliados, enquanto a Esquerda Neototalitária tenta, de forma patética, ligar a corrupção aos seus inimigos políticos.')">
                                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z"></path></svg>
                                <span>Copiar para WhatsApp</span>
                            </button>
                        </div>
                    </div>
"""
    # Replace content between <article... and </article>
    start_article = r'<!-- ARTIGO PRINCIPAL -->'
    end_article = r'<!-- BLOCO PREMIUM: RESUMO E ANÁLISE -->'
    
    match_start = re.search(start_article, html)
    match_end = re.search(end_article, html)
    
    if match_start and match_end:
        # We need to preserve the <article> tag from the original
        article_open = html[match_start.start():html.find('>', match_start.start())+1]
        html = html[:match_start.start()] + demolidor_content + "\n                " + html[match_end.start():]
        
        # We replace the summary blocks as well to match the Demolidor rule
        html = re.sub(r'<!-- BLOCO PREMIUM: RESUMO E ANÁLISE -->.*?</div>\s*</div>\s*</div>', '', html, flags=re.DOTALL)
        
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
        
if __name__ == '__main__':
    create_master_article()
