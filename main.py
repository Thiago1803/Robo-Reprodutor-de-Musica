import pygame
from view.sense_music import menuSentir
from view.act_talk import falarMensagens


def inicializarReprodutorMusica():
    # Inicialize o Pygame
    pygame.init()


def finalizarReprodutorMusica():
    # Encerra o Pygame
    pygame.quit()



inicializarReprodutorMusica()
falarMensagens("Olá, o que deseja?")
menuSentir()
finalizarReprodutorMusica()