from gtts import gTTS

text = """
Dossiê Tático: A Engenharia Social nas Pesquisas de Intenção de Voto.

O G1, atuando como braço de comunicação do Progressismo Autoritário, fatiou a pesquisa Quaest para fabricar uma manchete vitoriosa. Eles destacam um recorte hiper-específico, os chamados 'eleitores independentes', para criar a ilusão de que a oposição está derretendo.

A tática é simples: esconder o cenário geral e focar onde a máquina estatal tem peso. Essa é a Engenharia Social Coercitiva em ação. Ao associar episódios irrelevantes à suposta queda da direita, eles tentam criar uma falsa relação de causa e efeito, induzindo o leitor ao erro e desestimulando a base conservadora.

O nosso Manual de Defesa é claro: se a mídia precisa garimpar um único recorte estatístico para encontrar uma boa notícia para o governo, é porque o governo já fracassou. Não caia no efeito manada artificial criado pela esquerda neototalitária.
"""

tts = gTTS(text=text, lang='pt', tld='com.br', slow=False)
tts.save('d:/direita_intelectual/audio-quaest.mp3')
print("Áudio da Quaest gerado com sucesso!")
