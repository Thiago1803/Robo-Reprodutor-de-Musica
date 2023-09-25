import pygame
import os
from gtts import gTTS

def falarMensagens(mensagem):
    # Cria um objeto gTTS com o texto desejado e com idioma pt-br
    tts = gTTS(text=mensagem, lang='pt-br')

    pastaDestino = 'C:/Users/ricar/Documents/cpp/periodo 6/ia/TRABALHOIA/model/audioTemporario'
    if not os.path.exists(pastaDestino):
        os.makedirs(pastaDestino)

    # Define o nome do arquivo de áudio temporário
    nomeArquivo = "audio_temp.mp3"

    # Caminho completo para o arquivo de áudio
    caminhoCompleto = os.path.join(pastaDestino, nomeArquivo)

    # Salva o áudio no caminho especificado
    tts.save(caminhoCompleto)

    # Inicializa o mixer de áudio do pygame
    pygame.mixer.init()

    # Carrega o arquivo de áudio e reproduz
    pygame.mixer.music.load(caminhoCompleto)
    pygame.mixer.music.play()

    # Aguarda até que a reprodução termine
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)  # Pausa por um curto período de tempo

    # Exclui o arquivo temporário
    pygame.mixer.quit()