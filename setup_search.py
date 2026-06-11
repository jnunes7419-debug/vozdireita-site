import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update x-data
if "searchQuery: ''" not in content:
    content = content.replace(
        "searchOpen: false, mobileMenuOpen: false }",
        "searchOpen: false, mobileMenuOpen: false, searchQuery: '' }"
    )

# 2. Update search input
if "x-model=\"searchQuery\"" not in content:
    content = content.replace(
        '<input x-ref="searchInput" x-show="localSearchOpen"',
        '<input x-model="searchQuery" @input="window.scrollTo({top: document.getElementById(\'radar-narrativas\').offsetTop - 100, behavior: \'smooth\'})" x-ref="searchInput" x-show="localSearchOpen"'
    )

# 3. Add x-show to cards
card_start_str = 'backdrop-blur-md rounded-2xl overflow-hidden hover:-translate-y-2 hover:shadow-2xl hover:shadow-gold-500/5 hover:border-gold-500/30 transition-all duration-300 flex flex-col justify-between min-h-[440px] group"'

card_replacement = 'backdrop-blur-md rounded-2xl overflow-hidden hover:-translate-y-2 hover:shadow-2xl hover:shadow-gold-500/5 hover:border-gold-500/30 transition-all duration-300 flex flex-col justify-between min-h-[440px] group" x-transition x-show="searchQuery === \'\' || $el.textContent.toLowerCase().includes(searchQuery.toLowerCase())"'

if 'x-show="searchQuery' not in content:
    content = content.replace(card_start_str, card_replacement)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Search functionality added.")
