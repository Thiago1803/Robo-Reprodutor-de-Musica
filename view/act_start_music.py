import pygame
from view.sense_while_music_play import ouvirComMusica


def tocarMusica(path_musica):
    # Inicialize o Pygame
    pygame.init()

    # Carrega o arquivo de áudio desejado para tocar
    pygame.mixer.music.load(path_musica)

    # Reproduz o áudio
    pygame.mixer.music.play()

    # Se o canal de reprodução estiver tocando algo, vai continuar nesse loop
    while pygame.mixer.music.get_busy():
        ouvirComMusica()

#def dancar():