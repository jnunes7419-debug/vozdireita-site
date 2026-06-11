import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Move Hero Section
hero_start_marker = "<!-- HERO SECTION -->"
conteudos_start_marker = "<!-- CONTEÚDOS TÁTICOS -->"

hero_idx = content.find(hero_start_marker)
conteudos_idx = content.find(conteudos_start_marker)

if hero_idx != -1 and conteudos_idx != -1:
    hero_section = content[hero_idx:conteudos_idx]
    
    # Remove Hero Section from its original position
    content = content[:hero_idx] + content[conteudos_idx:]
    
    # Now find Biografia and replace it with Hero Section
    bio_start_marker = "<!-- SEÇÃO: O MENTOR (BIOGRAFIA) -->"
    footer_start_marker = "<!-- FOOTER (RODAPÉ) -->"
    
    bio_idx = content.find(bio_start_marker)
    footer_idx = content.find(footer_start_marker)
    
    if bio_idx != -1 and footer_idx != -1:
        # Replace bio with hero
        content = content[:bio_idx] + hero_section + "\n    " + content[footer_idx:]

# 2. Update Cookies
cookies_start = content.find("<!-- AVISO DE COOKIES (BOTTOM BAR) -->")
widget_start = content.find("<!-- INÍCIO DO WIDGET FLUTUANTE -->")

if cookies_start != -1 and widget_start != -1:
    old_cookies = content[cookies_start:widget_start]
    
    new_cookies = """<!-- AVISO DE COOKIES (BOTTOM BAR) -->
    <div x-data="{ showCookies: !sessionStorage.getItem('cookiesAccepted') }" 
         x-show="showCookies" 
         x-transition:enter="transition ease-out duration-300"
         x-transition:enter-start="opacity-0 translate-y-12"
         x-transition:enter-end="opacity-100 translate-y-0"
         x-transition:leave="transition ease-in duration-200"
         x-transition:leave-start="opacity-100 translate-y-0"
         x-transition:leave-end="opacity-0 translate-y-12"
         class="fixed bottom-4 right-4 left-4 md:left-auto md:w-[26rem] z-50 bg-[#fdfbf7] dark:bg-zinc-950 border border-zinc-200 dark:border-zinc-800 rounded-xl p-4 flex flex-col md:flex-row items-center justify-between gap-4 shadow-2xl text-zinc-800 dark:text-zinc-200"
         x-cloak>
        
        <p class="text-xs font-light max-w-sm text-center md:text-left leading-relaxed">
            Utilizamos cookies táticos para otimizar sua experiência no Centro de Inteligência. <a href="politica-privacidade" class="text-gold-600 dark:text-gold-400 font-bold hover:underline">Política</a>.
        </p>

        <div class="flex items-center shrink-0">
            <button @click="showCookies = false; sessionStorage.setItem('cookiesAccepted', 'true')" 
                    class="px-5 py-2 bg-gold-600 hover:bg-gold-500 text-white font-semibold text-xs uppercase tracking-wider rounded-lg transition-all shadow-md">
                Aceitar
            </button>
        </div>
    </div>

    """
    content = content.replace(old_cookies, new_cookies)

# 3. Update Widget
widget_end = content.find("<!-- FIM DO WIDGET FLUTUANTE -->")
if widget_start != -1 and widget_end != -1:
    old_widget = content[widget_start:widget_end + len("<!-- FIM DO WIDGET FLUTUANTE -->")]
    
    new_widget = """<!-- INÍCIO DO WIDGET FLUTUANTE -->
    <div x-data="{ showChat: !sessionStorage.getItem('welcomeChatShown') }" 
         x-show="showChat" 
         x-transition.opacity.duration.500ms
         class="fixed bottom-28 right-4 md:right-8 z-[9999] flex w-[calc(100vw-2rem)] sm:w-[320px] max-w-[320px] bg-[#fdfbf7] dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-800 shadow-2xl rounded-2xl p-4"
         style="display: none;">
         
         <button @click="showChat = false; sessionStorage.setItem('welcomeChatShown', 'true')" class="absolute top-2 right-2 text-zinc-400 hover:text-zinc-800 dark:hover:text-white transition-colors">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
         </button>

         <div class="flex items-center gap-3 pr-4">
            <div class="relative shrink-0">
                <img src="assets/jander_nunes_profile.png" alt="Jander Nunes" class="w-12 h-12 rounded-full object-cover border border-zinc-200 dark:border-white/20 shadow-inner">
                <span class="absolute bottom-0 right-0 w-3 h-3 bg-green-500 border-2 border-[#fdfbf7] dark:border-zinc-900 rounded-full"></span>
            </div>
            <div>
                <h4 class="text-zinc-900 dark:text-white font-bold text-sm tracking-wide">Jander Nunes</h4>
                <p class="text-zinc-600 dark:text-zinc-400 text-xs leading-tight mt-0.5">Bem-vindo. Nosso Centro de Inteligência está em fase final de construção.</p>
            </div>
         </div>
    </div>
    <!-- FIM DO WIDGET FLUTUANTE -->"""
    
    content = content.replace(old_widget, new_widget)

# Write modified content back
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Layout reorganized successfully.")
