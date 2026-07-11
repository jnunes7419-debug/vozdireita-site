import re

def main():
    with open('d:\\direita_intelectual\\analise-geopolitica-eua-brasil.html', 'r', encoding='utf-8') as f:
        html = f.read()

    titulo = 'Governo Trump convida Brasil para cúpula contra a "extrema-esquerda": A armadilha diplomática'
    subtitulo = 'A convocação de Washington expõe a hesitação da diplomacia brasileira e a escolha perigosa do governo frente ao extremismo transnacional.'

    # Fix the H1
    h1_pattern = r'(<h1[^>]*>).*?(</h1>)'
    html = re.sub(h1_pattern, rf'\g<1>{titulo}\g<2>', html, count=1, flags=re.DOTALL)

    # Fix the H2 (Subtitle)
    h2_pattern = r'(<h2[^>]*>).*?(</h2>)'
    html = re.sub(h2_pattern, rf'\g<1>{subtitulo}\g<2>', html, count=1, flags=re.DOTALL)

    with open('d:\\direita_intelectual\\analise-geopolitica-eua-brasil.html', 'w', encoding='utf-8') as f:
        f.write(html)

    print("Fixed title and subtitle in analise-geopolitica-eua-brasil.html")

if __name__ == '__main__':
    main()
