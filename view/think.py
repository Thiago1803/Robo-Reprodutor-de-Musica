import os
from view.act import *

# Pasta do projeto com as musicas
pasta = "/home/thiago/Área de Trabalho/TRABALHOIA/musicas"

musicaPausada = False
musicaIniciou = False


#MENU COM TRATAMENTO PARA OS COMANDOS 
#A primeira palavra que foi ouvida será o nome do robot e a segunda será o comando
def menu(textoEntendido):
    if(textoEntendido[0].lower() in "robô"):
        # Busca uma determinada musica para reproduzi-la
        if(textoEntendido[1].lower() in "tocar"):
            textoEntendido = textoEntendido[1:] #ignora a primeira palavra da lista, sobrando nome do cantor/banda e musica
            buscarMusica(textoEntendido)

        # Pausa uma musica que esta tocando
        elif(textoEntendido[1].lower() in "pausar"):
            pausar()
        
        # Volta a reproduzir a musica que foi pausada
        elif(textoEntendido[1].lower() in "continuar"):
            continuar()

        # Reproduz a playlist inteira
        elif(textoEntendido[1].lower() in "reproduzir"):
            reproduzirPlaylist()

        else:
            falarMensagens("Comando inexistente!")
    else:
        falarMensagens ("Nao entendi o que você disse, fale outra vez!")



#MUSICA
def pausar():
    if(musicaIniciou):
        pausarMusica()
        musicaPausada = True

def continuar():
    if(musicaPausada):
        continuarMusica()
        musicaPausada = False

def buscarMusica(nome):
    # Percorre todos os arquivos na pasta
    for arquivo in os.listdir(pasta):
        caminho_arquivo = os.path.join(pasta, arquivo)
        nome_arquivo, extensao= os.path.splitext(caminho_arquivo)

        # Transforma ambas strings em palavras com letras minusculas e compara se existe um arquivo com o nome informado
        if nome[0].lower() in nome_arquivo.lower():
            tocarMusica(caminho_arquivo)
            musicaIniciou = True
    
    if(musicaIniciou == False):
        falarMensagens("Musica nao encontrada!")
    else:
        musicaIniciou = False
    
def reproduzirPlaylist():
    # Percorre todos os arquivos na pasta e reproduz cada musica
    for arquivo in os.listdir(pasta):
        caminho_arquivo = os.path.join(pasta, arquivo)
        tocarMusica(caminho_arquivo)
        musicaIniciou = True

    if(musicaIniciou == False):
        falarMensagens("Playlist sem musicas!")
    else:
        musicaIniciou = False




#DANÇA