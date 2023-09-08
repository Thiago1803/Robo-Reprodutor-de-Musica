import pygame
from gtts import gTTS


def tocarMusica(path_musica):
    # Inicialize o Pygame
    pygame.init()

    # Carrega o arquivo de áudio desejado para tocar
    pygame.mixer.music.load(path_musica)

    # Reproduz o áudio
    pygame.mixer.music.play()

    # Mantenha o programa em execução para que o áudio continue tocando
    nome = input("Digite o que quer...")
    while(nome != "parar"):
        if nome == "pausar":
            pausarMusica()
        elif nome == "continuar":
            continuarMusica()
        nome = input("igite o que quer...")


    encerrarMusica()


def encerrarMusica():
    # Pare o áudio quando o usuário pressionar Enter
    pygame.mixer.music.stop()

    # Encerra o Pygame
    pygame.quit()


def pausarMusica():
    pygame.mixer.music.pause()


def continuarMusica():
    pygame.mixer.music.unpause()


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


#def dancar():