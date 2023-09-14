import pygame

def encerrarMusica():
    pygame.mixer.music.stop()


def pausarMusica():
    pygame.mixer.music.pause()


def continuarMusica():
    pygame.mixer.music.unpause()


def alterarVolume(volume):
    pygame.mixer.music.set_volume(volume)