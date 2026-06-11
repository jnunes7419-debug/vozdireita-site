import re

def main():
    file_path = 'd:\\direita_intelectual\\index.html'
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Add whitespace-nowrap to nav-link
    content = content.replace('class="nav-link ', 'class="nav-link whitespace-nowrap ')

    # 2. Change md:flex to lg:flex for the nav
    content = content.replace('<nav class="hidden md:flex items-center space-x-8">', '<nav class="hidden lg:flex items-center space-x-8 lg:space-x-6 xl:space-x-8">')

    # 3. Change md:hidden to lg:hidden for hamburger button
    # The hamburger button has: class="p-2 md:hidden text-zinc-600 ...
    content = content.replace('class="p-2 md:hidden text-zinc-600', 'class="p-2 lg:hidden text-zinc-600')

    # 4. Change md:hidden to lg:hidden for mobile drawer
    # The mobile drawer has: class="md:hidden border-t border-zinc-200/20 ...
    content = content.replace('class="md:hidden border-t border-zinc-200/20', 'class="lg:hidden border-t border-zinc-200/20')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print("Menu fixed.")

if __name__ == '__main__':
    main()
