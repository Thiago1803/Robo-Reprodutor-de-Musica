import pygame

def encerrarMusica():
    pygame.mixer.music.stop()
    
    # Encerra o Pygame
    pygame.quit()


def pausarMusica():
    pygame.mixer.music.pause()


def continuarMusica():
    pygame.mixer.music.unpause()