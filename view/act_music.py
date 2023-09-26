import os
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

def pularMusica(pasta):
    # Pule para a próxima música na pasta da playlist atual
    lista_musicas = os.listdir(pasta)
    musica_atual = pygame.mixer.music.get_busy()
    
    if musica_atual:
        pygame.mixer.music.stop()
    
    # Encontre a próxima música na lista
    if lista_musicas:
        index_musica_atual = lista_musicas.index(os.path.basename(musica_atual))
        if index_musica_atual < len(lista_musicas) - 1:
            proxima_musica = os.path.join(pasta, lista_musicas[index_musica_atual + 1])
            tocarMusica(proxima_musica)