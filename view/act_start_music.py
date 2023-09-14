import pygame
from view.sense_while_music_play import menuSentir
from view.act_while_music_play import encerrarMusica


def tocarMusica(path_musica):
    # Inicialize o Pygame
    pygame.init()

    # Carrega o arquivo de áudio desejado para tocar
    pygame.mixer.music.load(path_musica)

    # Reproduz o áudio
    pygame.mixer.music.play()

    # Se o canal de reprodução estiver tocando algo, vai continuar nesse loop
    menuSentir()

    if pygame.mixer.music.get_busy():
        encerrarMusica()
    
    # Encerra o Pygame
    pygame.quit()

#def dancar():