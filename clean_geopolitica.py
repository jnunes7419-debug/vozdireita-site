import re

def main():
    with open('d:\\direita_intelectual\\analise-geopolitica-eua-brasil.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Fix Tag (Cultura Pop -> Geopolítica)
    html = html.replace('>Cultura Pop<', '>Geopolítica<')

    # Remove the Manual de Defesa and the old Link since we already added the blocks 1, 2, 3 and 4 in the main prose.
    # Wait, the main prose was replaced, but the old "4. MANUAL DE DEFESA" was outside the prose block!
    # Let's remove the old "4. MANUAL DE DEFESA" completely, because the new "4. FONTE ORIGINAL" is inside the prose block!
    manual_defesa_pattern = r'<!-- 4\. MANUAL DE DEFESA -->.*?</div>\s*</div>\s*</div>\s*</main>'
    html = re.sub(manual_defesa_pattern, '</div>\n\n        </div>\n\n    </main>', html, flags=re.DOTALL)

    # Let's also remove the old Pull Quote if it still exists outside the new sections
    quote_pattern = r'<!-- Pull Quote Elegante -->.*?</blockquote>'
    html = re.sub(quote_pattern, '', html, flags=re.DOTALL)

    with open('d:\\direita_intelectual\\analise-geopolitica-eua-brasil.html', 'w', encoding='utf-8') as f:
        f.write(html)

    print("Cleaned up leftover elements in analise-geopolitica-eua-brasil.html")

if __name__ == '__main__':
    main()
