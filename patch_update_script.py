import re

def main():
    file_path = 'd:\\direita_intelectual\\update_home_cards.py'
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # We need to change the reconstruction loop to handle col-span-2 for the first card
    old_loop = """
    # Reconstruct the grid HTML with correct <!-- Card X -->
    new_grid_content = ""
    for i, c in enumerate(cards):
        new_grid_content += f"<!-- Card {i+1} -->\\n{c.strip()}\\n\\n"
"""

    new_loop = """
    # Reconstruct the grid HTML with correct <!-- Card X -->
    new_grid_content = ""
    for i, c in enumerate(cards):
        # Remove any existing col-span modifiers and taller image classes
        c = re.sub(r'\\s*md:col-span-2\\s+lg:col-span-[23]\\s*', ' ', c)
        c = c.replace('h-64 md:h-[22rem]', 'h-48')
        
        if i == 0:
            # Inject col-span-2 into the main div
            c = c.replace('class="bg-white/60', 'class="md:col-span-2 lg:col-span-2 bg-white/60')
            # Make image taller for the featured post
            c = c.replace('h-48', 'h-64 md:h-[22rem]')
            
        new_grid_content += f"<!-- Card {i+1} -->\\n{c.strip()}\\n\\n"
"""

    content = content.replace(old_loop.strip(), new_loop.strip())

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("update_home_cards.py updated successfully!")

if __name__ == '__main__':
    main()
