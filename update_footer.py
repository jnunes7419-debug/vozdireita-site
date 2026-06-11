import os
import glob
import re

old_social = """                <!-- Links de Redes Sociais -->
                <div class="flex items-center space-x-6">
                    <a href="#"
                        class="text-zinc-500 hover:text-gold-400 transition-colors text-xs uppercase tracking-wider font-semibold"
                        aria-label="X (antigo Twitter)">X (antigo Twitter)</a>
                    <a href="#"
                        class="text-zinc-500 hover:text-gold-400 transition-colors text-xs uppercase tracking-wider font-semibold"
                        aria-label="Telegram">Telegram</a>
                    <a href="#"
                        class="text-zinc-500 hover:text-gold-400 transition-colors text-xs uppercase tracking-wider font-semibold"
                        aria-label="YouTube">YouTube</a>
                </div>"""

new_social = """                <!-- Links de Redes Sociais (Ícones) -->
                <div class="flex items-center space-x-6">
                    <!-- X (Twitter) -->
                    <a href="#" class="text-zinc-500 hover:text-zinc-300 dark:hover:text-white transition-colors" aria-label="X (antigo Twitter)">
                        <svg class="h-5 w-5" fill="currentColor" viewBox="0 0 24 24">
                            <path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/>
                        </svg>
                    </a>
                    <!-- Telegram -->
                    <a href="#" class="text-zinc-500 hover:text-[#229ED9] transition-colors" aria-label="Telegram">
                        <svg class="h-5 w-5" fill="currentColor" viewBox="0 0 24 24">
                            <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm4.64 6.8c-.15 1.58-.8 5.42-1.13 7.19-.14.75-.42 1-.68 1.03-.58.05-1.02-.38-1.58-.75-.88-.58-1.38-.94-2.23-1.5-.99-.65-.35-1.01.22-1.59.15-.15 2.71-2.48 2.76-2.69a.2.2 0 00-.05-.18c-.06-.05-.14-.03-.21-.02-.09.02-1.49.95-4.22 2.79-.4.27-.76.41-1.08.4-.36-.01-1.04-.2-1.55-.37-.62-.2-1.12-.31-1.1-.66.01-.18.27-.36.78-.55 3.05-1.33 5.09-2.21 6.12-2.64 2.91-1.21 3.51-1.42 3.91-1.43.09 0 .28.02.4.11.1.08.13.19.14.28-.01.06.01.24-.03.38z"/>
                        </svg>
                    </a>
                    <!-- YouTube -->
                    <a href="#" class="text-zinc-500 hover:text-[#FF0000] transition-colors" aria-label="YouTube">
                        <svg class="h-5 w-5" fill="currentColor" viewBox="0 0 24 24">
                            <path d="M19.615 3.184c-3.604-.246-11.631-.245-15.23 0-3.897.266-4.356 2.62-4.385 8.816.029 6.185.484 8.549 4.385 8.816 3.6.245 11.626.246 15.23 0 3.897-.266 4.356-2.62 4.385-8.816-.029-6.185-.484-8.549-4.385-8.816zm-10.615 12.816v-8l8 3.993-8 4.007z"/>
                        </svg>
                    </a>
                </div>"""

back_to_top = """
    <!-- Botão Voltar ao Topo -->
    <button @click="window.scrollTo({top: 0, behavior: 'smooth'})"
            x-data="{ scrolled: false }"
            @scroll.window="scrolled = (window.pageYOffset > 300)"
            x-show="scrolled"
            x-transition:enter="transition ease-out duration-300"
            x-transition:enter-start="opacity-0 translate-y-10"
            x-transition:enter-end="opacity-100 translate-y-0"
            x-transition:leave="transition ease-in duration-300"
            x-transition:leave-start="opacity-100 translate-y-0"
            x-transition:leave-end="opacity-0 translate-y-10"
            class="fixed bottom-8 right-8 z-[100] p-3 bg-zinc-900/90 dark:bg-white/90 text-white dark:text-zinc-900 rounded-full shadow-2xl backdrop-blur-md hover:scale-110 hover:bg-gold-600 dark:hover:bg-gold-500 transition-all border border-zinc-700 dark:border-white/20"
            aria-label="Voltar ao topo" style="display: none;">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 10l7-7m0 0l7 7m-7-7v18" />
        </svg>
    </button>
</body>"""

for html_file in glob.glob("d:/direita_intelectual/*.html"):
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Apply Footer Icons
    if old_social in content:
        content = content.replace(old_social, new_social)
    
    # Check if back to top is already added
    if "Botão Voltar ao Topo" not in content:
        content = content.replace("</body>", back_to_top)
        
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Footer icons updated and Back to Top button added.")
