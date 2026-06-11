import re

with open('d:/direita_intelectual/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Fix radar-grid (keep exactly 7 cards: 1 large + 6 small)
grid_start_str = '<div id="radar-grid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">'
grid_start = content.find(grid_start_str)

if grid_start != -1:
    post_grid_idx = content.find('                                    </div>\n            </section>', grid_start)
    if post_grid_idx != -1:
        grid_content = content[grid_start + len(grid_start_str):post_grid_idx]
        parts = grid_content.split('<!-- Card')
        prefix = parts[0]
        cards_raw = parts[1:]
        
        cards = []
        for c in cards_raw:
            card_body = re.sub(r'^\s*\d+\s*(?:\([^)]+\))?\s*-->\s*', '', c, count=1)
            cards.append(card_body)
        
        # Keep only 7 cards
        if len(cards) > 7:
            cards = cards[:7]
        
        new_grid_content = prefix
        for i, c in enumerate(cards):
            new_grid_content += f"<!-- Card {i+1} -->\n{c}\n"
            
        content = content[:grid_start + len(grid_start_str)] + new_grid_content + content[post_grid_idx:]

# 2. Fix mais-artigos grid (keep exactly 6 items)
mini_grid_start_str = '<!-- Grid de Miniaturas -->\n                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">'
mini_start = content.find(mini_grid_start_str)

if mini_start != -1:
    post_mini_idx = content.find('                </div>\n            </section>', mini_start)
    if post_mini_idx != -1:
        mini_content = content[mini_start + len(mini_grid_start_str):post_mini_idx]
        parts = mini_content.split('<!-- Item')
        prefix = parts[0]
        items_raw = parts[1:]
        
        items = []
        for c in items_raw:
            item_body = re.sub(r'^\s*\d+\s*(?:\([^)]+\))?\s*-->\s*', '', c, count=1)
            items.append(item_body)
            
        # Keep only 6 items
        if len(items) > 6:
            items = items[:6]
            
        new_mini_content = prefix
        for i, c in enumerate(items):
            new_mini_content += f"<!-- Item {i+1} -->\n{c}\n"
            
        content = content[:mini_start + len(mini_grid_start_str)] + new_mini_content + content[post_mini_idx:]

with open('d:/direita_intelectual/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("index.html atualizado. Radar-grid tem", len(cards), "cards. Mais-artigos tem", len(items), "itens.")
