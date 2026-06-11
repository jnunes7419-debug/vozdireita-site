from gtts import gTTS

text = """
Dossiê Tático: A Engenharia Social Globalista contra Donald Trump e a FIFA.

O G1 ecoa a narrativa do jornal francês L'Équipe para construir a imagem de Donald Trump como um tirano e de Gianni Infantino, presidente da FIFA, como seu fantoche. Essa é a essência da Engenharia Social Coercitiva globalista.

A mídia internacional omite os motivos reais das restrições de fronteira dos Estados Unidos. Em vez de discutir segurança nacional, usam Adjetivos de Mancha, focando em casos individuais de atletas e árbitros para criar uma falsa aura de opressão institucional. 

O Neototalitarismo midiático precisa destruir qualquer líder que priorize a soberania de seu país em vez do espetáculo esportivo global. Nossa resposta deve expor a verdadeira intenção: a mídia não se importa com árbitros, ela se importa em minar líderes conservadores usando a emoção do esporte como arma.
"""

tts = gTTS(text=text, lang='pt', tld='com.br', slow=False)
tts.save('d:/direita_intelectual/audio-fifa-trump.mp3')
print("Áudio da FIFA gerado com sucesso!")
