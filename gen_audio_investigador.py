from gtts import gTTS

text = """
Dossiê Tático: A Falácia da Herança e a Agenda Oculta nas eleições do Peru.

A Carta Capital, atuando como braço do Foro de São Paulo, tenta esconder uma verdade inconveniente: os peruanos refugiados no Brasil votam massivamente na direita. Eles fugiram do laboratório socialista e rejeitam nas urnas quem causou seu próprio êxodo.

Para disfarçar isso, o veículo utiliza a falácia da Herança e Associação. Ao focar incessantemente no parentesco da candidata conservadora, a tática fica clara: O autor não tem argumentos contra as ideias da candidata, por isso recorre à tentativa de destruir sua honra através do passado de terceiros. 

Trata-se de Engenharia Social Coercitiva pura. Eles defendem a democracia apenas quando ela serve para manter a zona de influência da esquerda neototalitária. Nossa resposta deve ser implacável: apontar a falta de argumentos técnicos e expor a hipocrisia de quem tenta invalidar a direita com adjetivos de mancha, enquanto esconde o fracasso econômico de seus próprios aliados.
"""

tts = gTTS(text=text, lang='pt', tld='com.br', slow=False)
tts.save('d:/direita_intelectual/audio-peru.mp3')
print("Novo áudio gerado com base no Investigador!")
