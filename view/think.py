import os
from view.act import *

# Pasta do projeto com as musicas
pasta = "/home/thiago/Área de Trabalho/TRABALHOIA/musicas"


#MENU COM TRATAMENTO PARA OS COMANDOS 
#A primeira palavra que foi ouvida será o nome do robot e a segunda será o comando
def menuSemMusica(textoEntendido):
    if(textoEntendido[0].lower() in "robô"):
        if(textoEntendido[1].lower() not in "desligar"):
            # Busca uma determinada musica para reproduzi-la
            if(textoEntendido[1].lower() in "tocar"):
                textoEntendido = textoEntendido[2:] #ignora "robô" e "tocar" da lista, sobrando nome do cantor/banda e musica
                buscarMusica(textoEntendido)

            # Reproduz a playlist inteira
            elif(textoEntendido[1].lower() in "reproduzir"):
                reproduzirPlaylist()

            else:
                falarMensagens("Nao entendi o que você pediu, fale outra vez!")
        else:
            falarMensagens ("Desligando...")
    else:
        falarMensagens ("Está tentando falar comigo? Me chame pelo nome!")


def menuMusicaTocando(textoEntendido):
    if(textoEntendido[0].lower() in "robô"):
        if(textoEntendido[1].lower() not in "parar"):
            # Pausa a musica que esta tocando
            if(textoEntendido[1].lower() in "pausar"):
                pausar()
            
            # Volta a reproduzir a musica que foi pausada
            elif(textoEntendido[1].lower() in "continuar"):
                continuar()
            
            else:
                pausar()
                falarMensagens ("Nao entendi o que você pediu, fale outra vez!")
                continuar()
        else:
            pararMusica()




#MUSICA
def pausar():
    pausarMusica()

def continuar():
    continuarMusica()

def pararMusica():
    encerrarMusica()

def buscarMusica(nome):
    musicaIniciou = False
    # Percorre todos os arquivos na pasta
    for arquivo in os.listdir(pasta):
        caminho_arquivo = os.path.join(pasta, arquivo)
        nome_arquivo, extensao= os.path.splitext(caminho_arquivo)

        # Transforma ambas strings em palavras com letras minusculas e compara se existe um arquivo com o nome informado
        if nome[0].lower() in nome_arquivo.lower():
            tocarMusica(caminho_arquivo)
            musicaIniciou = True
    
    if(musicaIniciou == False):
        falarMensagens("Música nao encontrada!")
    else:
        musicaIniciou = False
    
def reproduzirPlaylist():
    musicaIniciou = False
    # Percorre todos os arquivos na pasta e reproduz cada musica
    for arquivo in os.listdir(pasta):
        caminho_arquivo = os.path.join(pasta, arquivo)
        tocarMusica(caminho_arquivo)
        musicaIniciou = True

    if(musicaIniciou == False):
        falarMensagens("Playlist sem músicas!")
    else:
        musicaIniciou = False




#DANÇA