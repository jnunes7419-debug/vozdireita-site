import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. We replace the search container definition
new_search_data = """<div class="relative flex items-center" x-data="{
    localSearchOpen: false,
    articles: [
        {
            title: 'Pais são condenados por homeschooling em SP',
            desc: 'A criminalização do ensino domiciliar através da Engenharia Social Coercitiva.',
            img: 'assets/homeschooling_condenacao.png',
            url: 'analise-g1-homeschooling.html',
            keywords: 'homeschooling jales sp são paulo pais condenados escola educação stf justiça liberdade ensino domiciliar'
        },
        {
            title: 'Messias rebate discurso de Flávio na Marcha',
            desc: 'Como a mídia blinda o governo e tenta interditar a indignação cristã.',
            img: 'assets/messias_marcha.png',
            url: 'analise-oglobo-messias.html',
            keywords: 'messias jorge messias flávio bolsonaro marcha para jesus evangélicos agu governo lula mídia'
        },
        {
            title: 'A Sabotagem Editorial do Roda Viva 2018',
            desc: 'Os bastidores das táticas inquisitoriais de debate.',
            img: 'assets/rodaviva_lobos.png',
            url: 'analise-rodaviva-bolsonaro.html',
            keywords: 'roda viva jair bolsonaro 2018 debate entrevista jornalismo aparelhado tv cultura eleições'
        },
        {
            title: 'Feitiço do terrorismo e Flávio Bolsonaro',
            desc: 'A esquerda neototalitária tenta criminalizar a oposição.',
            img: 'assets/seguranca_rj.png',
            url: 'analise-uol-terrorismo.html',
            keywords: 'terrorismo flávio bolsonaro uol segurança pública rio de janeiro milícia pcc crime organizado oposição'
        },
        {
            title: 'Decisão libera Monique Medeiros da prisão',
            desc: 'O progressismo autoritário e a anestesia da opinião pública.',
            img: 'assets/monique_liberada.png',
            url: 'analise-g1-monique.html',
            keywords: 'monique medeiros henry borel justiça soltura impunidade feminismo rio de janeiro crime'
        },
        {
            title: 'A Armadilha do Cavalo de Troia no PL',
            desc: 'Como a tornozeleira rosa cinde a base conservadora.',
            img: 'assets/tornozeleira_rosa.png',
            url: 'analise-oglobo-rosa.html',
            keywords: 'tornozeleira rosa pl 1811/2026 daniela reigner violência doméstica cavalo de troia direita mulher'
        }
    ],
    get filteredArticles() {
        if (searchQuery.trim() === '') return [];
        const q = searchQuery.toLowerCase();
        return this.articles.filter(a => (a.title + ' ' + a.desc + ' ' + a.keywords).toLowerCase().includes(q));
    }
}">"""

content = content.replace('<div class="relative flex items-center" x-data="{ localSearchOpen: false }">', new_search_data)

# 2. We replace the input field to remove the @input scrolling logic and add the dropdown template
# Find the start of the <input> up to x-cloak>
input_start = content.find('<input x-model="searchQuery"')
if input_start != -1:
    input_end = content.find('x-cloak>', input_start) + len('x-cloak>')
    
    new_input = """<input x-model="searchQuery" x-ref="searchInput" x-show="localSearchOpen" @click.away="if(searchQuery === '') localSearchOpen = false"
                        x-transition:enter="transition ease-out duration-300"
                        x-transition:enter-start="opacity-0 -translate-y-4 md:-translate-y-0 md:translate-x-4 md:scale-95"
                        x-transition:enter-end="opacity-100 translate-y-0 md:translate-x-0 md:scale-100"
                        x-transition:leave="transition ease-in duration-150"
                        x-transition:leave-start="opacity-100 translate-y-0 md:translate-x-0 md:scale-100"
                        x-transition:leave-end="opacity-0 -translate-y-2 md:-translate-y-0 md:translate-x-4 md:scale-95" type="text" id="input-search"
                        placeholder="Buscar inteligência..."
                        class="fixed top-[95px] left-4 right-4 md:absolute md:top-auto md:left-auto md:right-10 bg-white dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-800 text-sm md:text-xs px-4 py-2.5 md:py-1.5 rounded-xl md:rounded-full w-[calc(100vw-2rem)] md:w-64 focus:outline-none focus:border-gold-500 focus:ring-1 focus:ring-gold-500 shadow-2xl md:shadow-lg text-zinc-800 dark:text-zinc-200 z-[100] md:z-auto"
                        x-cloak>
                        
                    <!-- Janela de Resultados da Pesquisa (Dropdown) -->
                    <div x-show="searchQuery.length > 0 && localSearchOpen" 
                         class="fixed top-[145px] left-4 right-4 md:absolute md:top-full md:left-auto md:right-10 md:w-[320px] md:mt-4 bg-white/95 dark:bg-zinc-900/95 backdrop-blur-xl border border-zinc-200 dark:border-zinc-800 rounded-2xl shadow-2xl overflow-hidden z-[200] max-h-[60vh] overflow-y-auto"
                         x-transition:enter="transition ease-out duration-200"
                         x-transition:enter-start="opacity-0 translate-y-2"
                         x-transition:enter-end="opacity-100 translate-y-0"
                         x-transition:leave="transition ease-in duration-150"
                         x-transition:leave-start="opacity-100 translate-y-0"
                         x-transition:leave-end="opacity-0 translate-y-2"
                         x-cloak>
                        <div class="p-3 border-b border-zinc-100 dark:border-zinc-800 bg-zinc-50 dark:bg-zinc-800/50 flex justify-between items-center sticky top-0 z-10">
                            <span class="text-[10px] font-bold text-zinc-500 uppercase tracking-wider">Resultados Encontrados</span>
                            <span class="text-[10px] font-bold text-gold-600 dark:text-gold-500" x-text="filteredArticles.length + ' Dossiês'"></span>
                        </div>
                        
                        <template x-for="article in filteredArticles" :key="article.url">
                            <a :href="article.url" class="flex items-center p-4 border-b border-zinc-100 dark:border-zinc-800/50 hover:bg-zinc-50 dark:hover:bg-zinc-800/80 transition-colors group">
                                <div class="flex-shrink-0 pr-4">
                                    <img :src="article.img" class="w-14 h-14 md:w-12 md:h-12 object-cover rounded-md shadow-sm group-hover:scale-105 transition-transform">
                                </div>
                                <div class="flex-grow">
                                    <h4 class="text-sm font-bold text-zinc-900 dark:text-white leading-tight font-playfair group-hover:text-gold-600 dark:group-hover:text-gold-400 transition-colors" x-text="article.title"></h4>
                                    <p class="text-[11px] text-zinc-500 dark:text-zinc-400 mt-1 line-clamp-2 leading-relaxed" x-text="article.desc"></p>
                                </div>
                            </a>
                        </template>
                        
                        <div x-show="filteredArticles.length === 0" class="p-8 text-center">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8 mx-auto text-zinc-400 mb-3" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
                            </svg>
                            <p class="text-zinc-500 dark:text-zinc-400 text-xs font-medium">Nenhuma inteligência encontrada.</p>
                            <p class="text-zinc-400 dark:text-zinc-500 text-[10px] mt-1">Tente outros termos de busca.</p>
                        </div>
                    </div>"""
    
    content = content[:input_start] + new_input + content[input_end:]

# 3. Remove x-show filters from all cards
# We can just remove the string: x-show="searchQuery === '' || $el.textContent.toLowerCase().includes(searchQuery.toLowerCase())"
old_show_1 = 'x-show="searchQuery === \'\' || $el.textContent.toLowerCase().includes(searchQuery.toLowerCase())"'
old_show_2 = "x-show=\"searchQuery === '' || $el.textContent.toLowerCase().includes(searchQuery.toLowerCase())\""

content = content.replace(old_show_1, "")
content = content.replace(old_show_2, "")
content = content.replace('x-transition x-show=', '') # cleanup if any

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Dropdown search logic updated successfully.")
