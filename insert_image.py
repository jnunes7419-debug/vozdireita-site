import re

def main():
    file_path = 'D:\\direita_intelectual\\analise-carta-capital-pesquisa.html'
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    img_block = """
                    <div class="my-10 space-y-3">
                        <div class="border border-zinc-200 dark:border-white/10 rounded-3xl overflow-hidden shadow-2xl bg-zinc-950 relative group">
                            <div class="absolute inset-0 bg-gold-500/10 mix-blend-overlay opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
                            <img src="assets/grafico_pesquisa_es_1781048521496.png" 
                                 alt="Gráfico mostrando a liderança real camuflada pela mídia" 
                                 class="w-full h-auto object-cover max-h-[480px] transition-transform duration-500 group-hover:scale-[1.02]" loading="lazy" decoding="async">
                        </div>
                        <p class="text-xs text-zinc-500 font-mono tracking-wide text-center">
                            A verdadeira face dos números: A supressão de dados como arma de controle da percepção.
                        </p>
                    </div>
"""
    # Inserting the image block right before the closing </article> of the autopsia section
    content = re.sub(r'(</ul>\s*</article>)', img_block + r'\1', content, count=1)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    main()
