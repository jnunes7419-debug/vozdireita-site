import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Define the start of the grid
grid_start_str = '<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">'
grid_end_str = '</section>' # we will look for the closing div of the grid.

# Let's find the grid div
grid_start = content.find(grid_start_str)
if grid_start == -1:
    print("Grid not found")
    exit(1)

# The grid ends right before:
#                </div>
#            </section>
#            <!-- SEÇÃO 1: AUTÓPSIA DA MÍDIA -->

post_grid_idx = content.find('                </div>\n            </section>\n\n            <!-- SEÇÃO 1: AUTÓPSIA DA MÍDIA -->', grid_start)

if post_grid_idx == -1:
    print("Grid end not found")
    exit(1)

grid_content = content[grid_start + len(grid_start_str):post_grid_idx]

# Extract cards using regex: find <!-- Card X --> ... </div>
# Actually, since each card ends with '</div>\n\n                    <!-- Card' or the end of grid_content.
# Let's split by '<!-- Card'
parts = grid_content.split('<!-- Card')
prefix = parts[0]
cards_raw = parts[1:] # these start with ' 1 -->\n ...'

cards = []
for c in cards_raw:
    # remove the ' X -->' part at the beginning
    card_body = re.sub(r'^\s*\d+\s*(?:\([^)]+\))?\s*-->', '', c, count=1)
    cards.append(card_body)

print(f"Found {len(cards)} cards.")

if len(cards) > 0:
    # The last card added was Homeschooling (which should be first)
    last_card = cards.pop()
    cards.insert(0, last_card)
    
    # Enforce max 8 cards (if there were more than 8)
    if len(cards) > 8:
        cards = cards[:8]

    new_grid_content = prefix
    for i, c in enumerate(cards):
        # We need to preserve the <!-- Card X --> comment
        # In the original, the comment was sometimes <!-- Card 1 (Tornozeleira Rosa) -->
        new_grid_content += f"<!-- Card {i+1} -->{c}"
    
    # Replace in content
    new_content = content[:grid_start + len(grid_start_str)] + new_grid_content + content[post_grid_idx:]
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Cards reordered successfully. Total cards:", len(cards))
else:
    print("No cards found.")
