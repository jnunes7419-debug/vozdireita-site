import re

def main():
    file_path = 'd:\\direita_intelectual\\index.html'
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # The grid is between <!-- Grid de Miniaturas --> and </section> -> <!-- SEÇÃO 1: AUTÓPSIA DA MÍDIA -->
    start_pattern = r'<!-- Grid de Miniaturas -->\s*<div class="grid grid-cols-1 md:grid-cols-2 gap-4">\s*'
    end_pattern = r'\s*</div>\s*</section>\s*<!-- SEÇÃO 1: AUTÓPSIA DA MÍDIA -->'

    match_start = re.search(start_pattern, content)
    match_end = re.search(end_pattern, content)

    if not match_start or not match_end:
        print("Could not find thumbnails grid.")
        return

    items = [
        # Item 1: Roda Viva Bolsonaro
        """
                    <a href="analise-rodaviva-bolsonaro.html" class="flex items-center p-4 bg-white/60 dark:bg-white/5 border border-zinc-200 dark:border-white/10 backdrop-blur-md rounded-xl hover:-translate-y-1 hover:shadow-lg hover:border-gold-500/30 transition-all duration-300 group" >
                        <div class="flex-shrink-0 pr-4">
                            <img src="assets/rodaviva_lobos.png" alt="Miniatura" class="w-16 h-16 md:w-20 md:h-20 object-cover rounded-lg group-hover:scale-105 transition-all duration-300" loading="lazy">
                        </div>
                        <div class="flex-grow">
                            <h4 class="font-playfair text-sm md:text-base font-bold text-zinc-900 dark:text-white group-hover:text-gold-600 dark:group-hover:text-gold-400 transition-colors leading-snug">
                                A Sabotagem Editorial do Roda Viva 2018
                            </h4>
                            <p class="text-[11px] md:text-xs text-zinc-600 dark:text-zinc-400 font-light mt-2 line-clamp-2">
                                Os bastidores das táticas inquisitoriais de debate e a falência do modelo isento.
                            </p>
                        </div>
                    </a>
        """,
        # Item 2: UOL Terrorismo
        """
                    <a href="analise-uol-terrorismo.html" class="flex items-center p-4 bg-white/60 dark:bg-white/5 border border-zinc-200 dark:border-white/10 backdrop-blur-md rounded-xl hover:-translate-y-1 hover:shadow-lg hover:border-gold-500/30 transition-all duration-300 group" >
                        <div class="flex-shrink-0 pr-4">
                            <img src="assets/seguranca_rj.png" alt="Miniatura" class="w-16 h-16 md:w-20 md:h-20 object-cover rounded-lg group-hover:scale-105 transition-all duration-300" loading="lazy">
                        </div>
                        <div class="flex-grow">
                            <h4 class="font-playfair text-sm md:text-base font-bold text-zinc-900 dark:text-white group-hover:text-gold-600 dark:group-hover:text-gold-400 transition-colors leading-snug">
                                O Feitiço do Terrorismo e Flávio Bolsonaro
                            </h4>
                            <p class="text-[11px] md:text-xs text-zinc-600 dark:text-zinc-400 font-light mt-2 line-clamp-2">
                                A esquerda neototalitária tenta criminalizar a oposição através de manobras jurídicas.
                            </p>
                        </div>
                    </a>
        """,
        # Item 3: Oglobo Messias
        """
                    <a href="analise-oglobo-messias.html" class="flex items-center p-4 bg-white/60 dark:bg-white/5 border border-zinc-200 dark:border-white/10 backdrop-blur-md rounded-xl hover:-translate-y-1 hover:shadow-lg hover:border-gold-500/30 transition-all duration-300 group" >
                        <div class="flex-shrink-0 pr-4">
                            <img src="assets/messias_marcha.png" alt="Miniatura" class="w-16 h-16 md:w-20 md:h-20 object-cover rounded-lg group-hover:scale-105 transition-all duration-300" loading="lazy">
                        </div>
                        <div class="flex-grow">
                            <h4 class="font-playfair text-sm md:text-base font-bold text-zinc-900 dark:text-white group-hover:text-gold-600 dark:group-hover:text-gold-400 transition-colors leading-snug">
                                Jorge Messias e a Blindagem na Marcha para Jesus
                            </h4>
                            <p class="text-[11px] md:text-xs text-zinc-600 dark:text-zinc-400 font-light mt-2 line-clamp-2">
                                Como a mídia blinda o governo e tenta interditar a indignação cristã legítima.
                            </p>
                        </div>
                    </a>
        """,
        # Item 4: UOL Marcha Para Jesus
        """
                    <a href="analise-uol-marcha.html" class="flex items-center p-4 bg-white/60 dark:bg-white/5 border border-zinc-200 dark:border-white/10 backdrop-blur-md rounded-xl hover:-translate-y-1 hover:shadow-lg hover:border-gold-500/30 transition-all duration-300 group" >
                        <div class="flex-shrink-0 pr-4">
                            <img src="assets/studio_uol_news.png" alt="Miniatura" class="w-16 h-16 md:w-20 md:h-20 object-cover rounded-lg group-hover:scale-105 transition-all duration-300" loading="lazy">
                        </div>
                        <div class="flex-grow">
                            <h4 class="font-playfair text-sm md:text-base font-bold text-zinc-900 dark:text-white group-hover:text-gold-600 dark:group-hover:text-gold-400 transition-colors leading-snug">
                                A Redução do Engajamento na Marcha para Jesus
                            </h4>
                            <p class="text-[11px] md:text-xs text-zinc-600 dark:text-zinc-400 font-light mt-2 line-clamp-2">
                                A engenharia social para enfraquecer o conservadorismo no Brasil.
                            </p>
                        </div>
                    </a>
        """,
        # Item 5: UOL Posse Lula
        """
                    <a href="analise-uol-lula.html" class="flex items-center p-4 bg-white/60 dark:bg-white/5 border border-zinc-200 dark:border-white/10 backdrop-blur-md rounded-xl hover:-translate-y-1 hover:shadow-lg hover:border-gold-500/30 transition-all duration-300 group" >
                        <div class="flex-shrink-0 pr-4">
                            <img src="assets/newsroom_banner.png" alt="Miniatura" class="w-16 h-16 md:w-20 md:h-20 object-cover rounded-lg group-hover:scale-105 transition-all duration-300" loading="lazy">
                        </div>
                        <div class="flex-grow">
                            <h4 class="font-playfair text-sm md:text-base font-bold text-zinc-900 dark:text-white group-hover:text-gold-600 dark:group-hover:text-gold-400 transition-colors leading-snug">
                                O Simbolismo da Posse de Lula
                            </h4>
                            <p class="text-[11px] md:text-xs text-zinc-600 dark:text-zinc-400 font-light mt-2 line-clamp-2">
                                Uma autópsia das imagens fabricadas para legitimar um retorno ao poder sem respaldo nas ruas.
                            </p>
                        </div>
                    </a>
        """,
        # Item 6: Padrão
        """
                    <a href="analise-padrao.html" class="flex items-center p-4 bg-white/60 dark:bg-white/5 border border-zinc-200 dark:border-white/10 backdrop-blur-md rounded-xl hover:-translate-y-1 hover:shadow-lg hover:border-gold-500/30 transition-all duration-300 group" >
                        <div class="flex-shrink-0 pr-4">
                            <img src="assets/media_autopsy.png" alt="Miniatura" class="w-16 h-16 md:w-20 md:h-20 object-cover rounded-lg group-hover:scale-105 transition-all duration-300" loading="lazy">
                        </div>
                        <div class="flex-grow">
                            <h4 class="font-playfair text-sm md:text-base font-bold text-zinc-900 dark:text-white group-hover:text-gold-600 dark:group-hover:text-gold-400 transition-colors leading-snug">
                                Como Operam as Agências de "Fact-Checking"
                            </h4>
                            <p class="text-[11px] md:text-xs text-zinc-600 dark:text-zinc-400 font-light mt-2 line-clamp-2">
                                A ilusão da isenção e o monopólio da verdade na era da guerra de informações.
                            </p>
                        </div>
                    </a>
        """
    ]

    new_grid_content = ""
    for i, item in enumerate(items):
        new_grid_content += f"<!-- Item {i+1} -->\n{item.strip()}\n\n"

    new_content = content[:match_start.end()] + new_grid_content + content[match_end.start():]

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print("Thumbnails rebuilt successfully!")

if __name__ == '__main__':
    main()
