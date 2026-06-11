import io

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# We need to replace the search input block
old_input_str = """                    <input x-model="searchQuery" @input="if(searchQuery.length > 0) { let target = window.innerWidth < 768 ? 'radar-grid' : 'radar-narrativas'; window.scrollTo({top: document.getElementById(target).getBoundingClientRect().top + window.scrollY - 100, behavior: 'smooth'}) }" x-ref="searchInput" x-show="localSearchOpen" @click.away="localSearchOpen = false"
                        x-transition:enter="transition ease-out duration-200"
                        x-transition:enter-start="opacity-0 scale-95 translate-x-4"
                        x-transition:enter-end="opacity-100 scale-100 translate-x-0"
                        x-transition:leave="transition ease-in duration-150"
                        x-transition:leave-start="opacity-100 scale-100 translate-x-0"
                        x-transition:leave-end="opacity-0 scale-95 translate-x-4" type="text" id="input-search"
                        placeholder="Buscar inteligência..."
                        class="absolute right-10 bg-white dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-800 text-xs px-3 py-1.5 rounded-full w-48 md:w-64 focus:outline-none focus:border-gold-500 focus:ring-1 focus:ring-gold-500 shadow-lg text-zinc-800 dark:text-zinc-200"
                        x-cloak>"""

new_input_str = """                    
                    <!-- SVG Linha de Ramificação (Mobile Apenas) -->
                    <svg x-show="localSearchOpen" class="fixed top-[60px] right-[60px] w-[30px] h-[35px] z-40 md:hidden pointer-events-none text-gold-500/60 dark:text-gold-500/40" viewBox="0 0 30 35" fill="none" stroke="currentColor" stroke-width="1.5"
                        x-transition:enter="transition-opacity ease-out duration-500 delay-100"
                        x-transition:enter-start="opacity-0"
                        x-transition:enter-end="opacity-100"
                        x-transition:leave="transition-opacity ease-in duration-150"
                        x-transition:leave-start="opacity-100"
                        x-transition:leave-end="opacity-0"
                        x-cloak>
                        <path d="M 20,0 C 20,15 0,20 0,35" />
                    </svg>

                    <input x-model="searchQuery" @input="if(searchQuery.length > 0) { let target = window.innerWidth < 768 ? 'radar-grid' : 'radar-narrativas'; window.scrollTo({top: document.getElementById(target).getBoundingClientRect().top + window.scrollY - 100, behavior: 'smooth'}) }" x-ref="searchInput" x-show="localSearchOpen" @click.away="localSearchOpen = false"
                        x-transition:enter="transition ease-out duration-300"
                        x-transition:enter-start="opacity-0 -translate-y-4 md:-translate-y-0 md:translate-x-4 md:scale-95"
                        x-transition:enter-end="opacity-100 translate-y-0 md:translate-x-0 md:scale-100"
                        x-transition:leave="transition ease-in duration-150"
                        x-transition:leave-start="opacity-100 translate-y-0 md:translate-x-0 md:scale-100"
                        x-transition:leave-end="opacity-0 -translate-y-2 md:-translate-y-0 md:translate-x-4 md:scale-95" type="text" id="input-search"
                        placeholder="Buscar inteligência..."
                        class="fixed top-[95px] left-4 right-4 md:absolute md:top-auto md:left-auto md:right-10 bg-white dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-800 text-sm md:text-xs px-4 py-2.5 md:py-1.5 rounded-xl md:rounded-full w-[calc(100vw-2rem)] md:w-64 focus:outline-none focus:border-gold-500 focus:ring-1 focus:ring-gold-500 shadow-2xl md:shadow-lg text-zinc-800 dark:text-zinc-200 z-[100] md:z-auto"
                        x-cloak>"""

if old_input_str in content:
    content = content.replace(old_input_str, new_input_str)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Mobile search input UI updated successfully.")
else:
    print("Old input string not found.")
