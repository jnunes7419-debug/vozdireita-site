import os
import sys

try:
    from gtts import gTTS
except ImportError:
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "gTTS"])
    from gtts import gTTS

texto = """A manchete oficial diz: Como está a disputa entre Keiko Fujimori e Sánchez entre peruanos de 11 capitais brasileiras. A premissa falsa é que a mídia usa uma linguagem asséptica e matemática para esconder o pânico diante da rejeição expressiva que a esquerda enfrenta entre expatriados sul-americanos. Na nossa autópsia do fato, revelamos a realidade oculta. Primeiro, o exílio como sintoma: omitem que os peruanos no Brasil são vítimas econômicas fugindo da instabilidade. Segundo, o paradoxo do voto progressista: escondem que a esquerda é brutalmente rejeitada por quem vive a realidade fora da bolha. E terceiro, a maquiagem estatística: celebram a liderança de Sánchez para invisibilizar que o imigrante trabalhador rejeita o projeto da esquerda. O diagnóstico da tática aponta para a Esquerda Neototalitária, que utiliza o Filtro Estatístico Asséptico. Trata-se de uma Engenharia Social Coercitiva sutil, protegendo a hegemonia de seu próprio projeto ideológico. No nosso manual de defesa, a arma intelectual é clara: A mídia celebra os cinquenta por cento da esquerda no Peru, mas esconde por que cinquenta e cinco por cento dos peruanos que fugiram para o Brasil votaram contra eles. Quem foge do laboratório socialista na América Latina nunca vota no Progressismo Autoritário, vota na direita para sobreviver. Usar números para esconder esse pânico é pura Engenharia Social Coercitiva."""

tts = gTTS(text=texto, lang='pt', tld='com.br')
tts.save("d:/direita_intelectual/audio-peru.mp3")
print("Áudio gerado com sucesso!")
