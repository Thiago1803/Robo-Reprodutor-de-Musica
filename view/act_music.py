import pygame

def tocarMusica(path_musica):
    # Carrega o arquivo de áudio desejado para tocar
    pygame.mixer.music.load(path_musica)

    # Reproduz o áudio
    pygame.mixer.music.play()


def encerrarMusica():
    pygame.mixer.music.stop()


def pausarMusica():
    pygame.mixer.music.pause()


def continuarMusica():
    pygame.mixer.music.unpause()


def alterarVolume(volume):
    pygame.mixer.music.set_volume(volume)


def musicaTocando():
    return pygame.mixer.music.get_busy()