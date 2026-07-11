import re

def main():
    file_path = 'd:\\direita_intelectual\\analise-geopolitica-eua-brasil.html'
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()

    new_content = """
            <!-- COLUNA CENTRAL (O Artigo) -->
            <div class="lg:col-span-8 2xl:col-span-7 space-y-12">

                <!-- 1. O FATO ANALISADO -->
                <article id="artigo-inicio" class="prose prose-zinc dark:prose-invert max-w-none text-lg md:text-xl leading-relaxed font-jakarta font-light text-zinc-800 dark:text-zinc-300 scroll-mt-24
                    prose-p:mb-8 prose-strong:text-zinc-900 dark:prose-strong:text-white prose-strong:font-semibold">
                    
                    <h3 class="font-playfair text-3xl font-bold text-zinc-900 dark:text-white mb-6 border-l-4 border-gold-500 pl-4">
                        1. O FATO ANALISADO
                    </h3>
                    
                    <div class="p-6 bg-zinc-100 dark:bg-zinc-900/50 rounded-lg border border-zinc-200 dark:border-zinc-800 mb-8 italic">
                        O governo Trump estendeu um convite oficial ao Brasil para integrar uma cúpula internacional focada no combate ao terrorismo de "extrema-esquerda", colocando a gestão petista sob escrutínio diplomático direto de Washington.
                    </div>
                    
                    <p>
                        A convocação para o evento representa um movimento de alinhamento geopolítico claro. Ao formatar a cúpula com foco explícito no combate à "extrema-esquerda", Washington força nações a se posicionarem publicamente sobre o terrorismo com motivação ideológica de cunho marxista. Para o Brasil, o convite não é apenas uma formalidade diplomática, mas uma armadilha tática. Obriga a atual administração a escolher entre endossar uma pauta diametralmente oposta às suas alianças históricas na América Latina (como o Foro de São Paulo) ou declinar o convite, isolando o país do bloco conservador hemisférico e confirmando a simpatia do governo pela agenda progressista radical.
                    </p>

                </article>

                <!-- 2. A BASE LEGAL E CONSTITUCIONAL -->
                <article id="realidade-oculta" class="prose prose-zinc dark:prose-invert max-w-none text-lg md:text-xl leading-relaxed font-jakarta font-light text-zinc-800 dark:text-zinc-300 scroll-mt-24
                    prose-p:mb-8 prose-strong:text-zinc-900 dark:prose-strong:text-white prose-strong:font-semibold mt-16">
                    
                    <h3 class="font-playfair text-3xl font-bold text-zinc-900 dark:text-white mb-6 border-l-4 border-gold-500 pl-4">
                        2. A BASE LEGAL E CONSTITUCIONAL
                    </h3>
                    
                    <p>
                        Segundo o Artigo 84 da Constituição Federal, compete privativamente ao Presidente da República manter relações com Estados estrangeiros e dirigir a política externa brasileira. Entretanto, o Artigo 4º, que rege as relações internacionais, exige a "repúdio ao terrorismo e ao racismo". 
                    </p>
                    <p>
                        A recusa ou aceitação do convite entra no campo da prerrogativa do Executivo, porém uma eventual rejeição motivada pela recusa em enquadrar grupos de "extrema-esquerda" como terroristas evidenciará um desvio de finalidade diplomática. A omissão em colaborar contra o extremismo transnacional, caso o governo opte por boicotar o evento, demonstra o uso do Itamaraty para proteção de aliados ideológicos em detrimento dos princípios constitucionais de segurança hemisférica.
                    </p>

                </article>

                <!-- Pull Quote Elegante -->
                <blockquote class="relative my-16 p-8 md:p-12 text-center bg-zinc-100/50 dark:bg-zinc-900/30 rounded-3xl border border-zinc-200/50 dark:border-white/5 shadow-inner">
                    <svg class="absolute top-4 left-6 w-12 h-12 text-gold-500/20" fill="currentColor" viewBox="0 0 24 24"><path d="M14.017 21v-7.391c0-5.704 3.731-9.57 8.983-10.609l.995 2.151c-2.432.917-3.995 3.638-3.995 5.849h4v10h-9.983zm-14.017 0v-7.391c0-5.704 3.748-9.57 9-10.609l.996 2.151c-2.433.917-3.996 3.638-3.996 5.849h3.983v10h-9.983z"/></svg>
                    <p class="font-playfair text-2xl md:text-3xl font-medium text-zinc-900 dark:text-gold-400 italic mb-0 leading-tight">
                        "O convite de Trump não é um aceno; é um teste de estresse tático. A resposta do Planalto revelará se a política externa serve ao Brasil ou se atua como escudo para o Foro de São Paulo."
                    </p>
                </blockquote>

                <!-- 3. A ANÁLISE DE IMPACTO -->
                <article id="diagnostico" class="prose prose-zinc dark:prose-invert max-w-none text-lg md:text-xl leading-relaxed font-jakarta font-light text-zinc-800 dark:text-zinc-300 scroll-mt-24
                    prose-p:mb-8 prose-strong:text-zinc-900 dark:prose-strong:text-white prose-strong:font-semibold">
                    
                    <h3 class="font-playfair text-3xl font-bold text-zinc-900 dark:text-white mb-6 border-l-4 border-gold-500 pl-4">
                        3. A ANÁLISE DE IMPACTO
                    </h3>

                    <p>
                        A probabilidade de o atual governo brasileiro comparecer ou apoiar substancialmente a pauta desta cúpula é quase nula. O alinhamento ideológico <strong>Neototalitário</strong> exige a proteção das milícias políticas que sustentam regimes aliados na América do Sul. A recusa ou o rebaixamento da delegação enviada sinalizará a consolidação de um distanciamento pragmático entre Brasília e a administração Trump.
                    </p>
                    <p>
                        Este fato desmorona as narrativas de que o atual governo busca uma política externa isenta e multipolar. Revela, na prática, que o Itamaraty opera sob a égide da solidariedade partidária transnacional. Ao se afastar de uma aliança de inteligência e segurança capitaneada pela maior economia do mundo, o Brasil adota uma postura que privilegia a proteção estética de movimentos extremistas aliados em detrimento da segurança hemisférica real.
                    </p>

                </article>

                <!-- 4. FONTE ORIGINAL -->
                <div id="manual" class="mt-16 space-y-12 scroll-mt-24">
                    
                    <!-- Fonte do Artigo -->
                    <div class="mt-12 text-right">
                        <a href="https://www.metropoles.com/mundo/governo-trump-convida-brasil-para-evento-contra-a-extrema-esquerda" target="_blank" rel="noopener noreferrer" class="inline-flex items-center text-sm font-mono text-zinc-500 hover:text-gold-500 transition-colors group">
                            <span>Metrópoles | Acesse a matéria original aqui</span>
                            <svg class="w-4 h-4 ml-2 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
                        </a>
                    </div>

                </div>

            </div>
"""

    pattern = r'<!-- COLUNA CENTRAL \(O Artigo\) -->.*?</div>\s*</div>\s*</main>'
    new_html = re.sub(pattern, new_content.strip() + '\n\n        </div>\n\n    </main>', html, flags=re.DOTALL)

    # Let's fix the Index links too
    index_pattern = r'<!-- Indicador de Progresso \(Simulado\) e Links -->.*?</div>\s*</aside>'
    new_index = """<!-- Indicador de Progresso (Simulado) e Links -->
                    <div class="hidden xl:block">
                        <h4 class="text-xs font-bold uppercase tracking-widest text-zinc-400 mb-4 border-b border-zinc-200 dark:border-zinc-800 pb-2">Índice da Autópsia</h4>
                        <ul class="space-y-3 text-sm font-jakarta text-zinc-500 dark:text-zinc-400">
                            <li><a href="#artigo-inicio" class="hover:text-gold-500 transition-colors flex items-center"><span class="w-1.5 h-1.5 rounded-full bg-gold-500 mr-2"></span> O Fato Analisado</a></li>
                            <li><a href="#realidade-oculta" class="hover:text-gold-500 transition-colors flex items-center"><span class="w-1.5 h-1.5 rounded-full bg-zinc-300 dark:bg-zinc-700 mr-2"></span> A Base Legal</a></li>
                            <li><a href="#diagnostico" class="hover:text-gold-500 transition-colors flex items-center"><span class="w-1.5 h-1.5 rounded-full bg-zinc-300 dark:bg-zinc-700 mr-2"></span> A Análise de Impacto</a></li>
                            <li><a href="#manual" class="hover:text-gold-500 transition-colors flex items-center"><span class="w-1.5 h-1.5 rounded-full bg-zinc-300 dark:bg-zinc-700 mr-2"></span> Fonte Original</a></li>
                        </ul>
                    </div>

                </div>
            </aside>"""
    new_html = re.sub(index_pattern, new_index, new_html, flags=re.DOTALL)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_html)

    print("Replaced all Dark Horse content with Geopolitics content")

if __name__ == '__main__':
    main()
