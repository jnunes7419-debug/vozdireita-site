import re

def main():
    file_path = 'd:\\direita_intelectual\\index.html'
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    new_article = """
        {
            title: 'Pesquisa ES: A Manobra da Supressão de Horizonte',
            desc: 'A disputa entre Lula e Flávio Bolsonaro no Espírito Santo e a manipulação do empate técnico.',
            img: 'assets/grafico_pesquisa_es_1781048521496.png',
            url: 'analise-carta-capital-pesquisa.html'
        },"""

    # We will search for "articles: [" and insert our new article right after it
    # But let's check if it's already there
    # Check if we already have it in the articles array
    match = re.search(r'articles:\s*\[(.*?)\]', content, re.DOTALL)
    if match and 'analise-carta-capital-pesquisa.html' not in match.group(1):
        content = re.sub(r'(articles:\s*\[)', r'\1\n' + new_article + ',', content)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Search updated successfully.")
    else:
        print("File might already contain this article in the search.")
        
if __name__ == '__main__':
    main()
