import pygame
from gtts import gTTS

def falarMensagens(mensagem):
    # Cria um objeto gTTS com o texto desejado e com idioma pt-br
    tts = gTTS(text=mensagem, lang='pt-br')

    # Salva o áudio em um arquivo temporário
    tts.save("audio_temp.mp3")

    # Inicializa o mixer de áudio do pygame
    pygame.mixer.init()

    # Carrega o arquivo de áudio e reproduz
    pygame.mixer.music.load("audio_temp.mp3")
    pygame.mixer.music.play()

    # Aguarda até que a reprodução termine
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)  # Pausa por um curto período de tempo

    # Exclui o arquivo temporário
    pygame.mixer.quit()