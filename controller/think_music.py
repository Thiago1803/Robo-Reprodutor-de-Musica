import os
import threading
import time
from view.act_music import *
from view.act_talk import *

# Pasta do projeto com as musicas
pastaMusicas = "/home/thiago/Área de Trabalho/TRABALHOIA/model/musicas"
pastaPlaylists = "/home/thiago/Área de Trabalho/TRABALHOIA/model/playlists"
musicaPausada = False
musicaParada = False


# Envia mensagens de erro ou de despedida para o robô falar
def menuParaMensagens(mensagem):
    falarMensagens(mensagem)


# Verifica se a pasta de musicas esta vazia
def verificarPlaylist(pasta):
    if not os.listdir(pasta):
        menuParaMensagens("Playlist inexistente ou sem músicas!")
        return -1
    
    return 1


def verificarMusicaTocando():
    return musicaTocando()


def verificarMusicaPausada():
    global musicaPausada
    return musicaPausada



#MENU COM TRATAMENTO PARA OS COMANDOS QUANDO NÃO ESTA TOCANDO NENHUMA MUSICA
#A primeira palavra que foi ouvida será o nome do robô e a segunda será o comando

def menuSemMusica(textoEntendido):
    global musicaParada
    if("desligar" not in textoEntendido and "Desligar" not in textoEntendido):
        musicaParada = False
        # Busca uma determinada musica para reproduzi-la
        if("tocar" in textoEntendido or "Tocar" in textoEntendido):
            if("todas" in textoEntendido or "Todas" in textoEntendido):
                threading.Thread(target=reproduzirTodasMusicas).start()
            else:
                textoEntendido = textoEntendido[1:] #ignora "tocar" da lista, sobrando nome do cantor/banda e musica
                separator = '' #indica como irá separar as palavras da lista, no caso é sem espaço
                musica = [separator.join(textoEntendido)] #concatena todas as palavras da lista
                buscarMusica(musica)

        elif(("reproduzir" in textoEntendido or "Reproduzir" in textoEntendido) and ("playlist" in textoEntendido or "Playlist" in textoEntendido)):
            textoEntendido = textoEntendido[2:] #ignora "reproduzir" e "playlist" da lista, sobrando nome da playlist
            separator = '' #indica como irá separar as palavras da lista, no caso é sem espaço
            playlist = [separator.join(textoEntendido)] #concatena todas as palavras da lista
            threading.Thread(target=reproduzirPlaylist, args=playlist).start()  # Passar a pasta como argumento
        
    else:
        menuParaMensagens("Desligando... Até mais!")

    

def buscarMusica(nome):
    if verificarPlaylist(pastaMusicas) == 1:
        #Variavel de controle para indicar se a musica foi encontrada ou nao
        musicaIniciou = False

        # Percorre todos os arquivos na pasta, reproduzindo a musica desejada caso for encontrada
        for arquivo in os.listdir(pastaMusicas):
            caminho_arquivo = os.path.join(pastaMusicas, arquivo)
            nome_arquivo, extensao= os.path.splitext(caminho_arquivo)

            # Transforma ambas strings em palavras com letras minusculas e compara se existe um arquivo com o nome informado
            if nome[0].lower() in nome_arquivo.lower():
                tocarMusica(caminho_arquivo)
                musicaIniciou = True
        
        if(musicaIniciou == False):
            menuParaMensagens("Música nao encontrada!")
        else:
            musicaIniciou = False
    


def reproduzirPlaylist(nome):
    global musicaParada
    if verificarPlaylist(pastaPlaylists) == 1:
        # Percorre todos os arquivos na pasta, reproduzindo a musica desejada caso for encontrada
        for arquivo in os.listdir(pastaPlaylists):
            caminho_playlist = os.path.join(pastaPlaylists, arquivo)

            # Transforma ambas strings em palavras com letras minusculas e compara se existe um arquivo com o nome informado
            if nome[0].lower() in caminho_playlist.lower():
                if verificarPlaylist(caminho_playlist) == 1:
                    for arquivo in os.listdir(caminho_playlist):
                        if(musicaParada == False):
                            caminho_arquivo = os.path.join(caminho_playlist, arquivo)
                            tocarMusica(caminho_arquivo)
                            while(verificarMusicaTocando() or verificarMusicaPausada()):
                                continue
                        
                
                break
    else:
        menuParaMensagens("Você não criou nenhuma playlist!")


def reproduzirTodasMusicas():
    global musicaParada
    if verificarPlaylist(pastaMusicas) == 1:
        # Percorre todos os arquivos na pasta, reproduzindo cada musica
        for arquivo in os.listdir(pastaMusicas):
            if(musicaParada == False):
                caminho_arquivo = os.path.join(pastaMusicas, arquivo)
                tocarMusica(caminho_arquivo)
                while(verificarMusicaTocando() or verificarMusicaPausada()):
                    continue





def menuMusicaTocando(textoEntendido):
    global musicaPausada
    global musicaParada
    
    if("parar" not in textoEntendido and "Parar" not in textoEntendido):
        # Se uma musica estiver tocando, ela será pausada
        if("pausar" in textoEntendido or "Pausar" in textoEntendido):
            if musicaPausada == False:
                musicaPausada = True
                pausar()
        
        # Se uma musica foi pausada, ela voltara a tocar
        elif("continuar" in textoEntendido or "Continuar" in textoEntendido):
            if musicaPausada == True:
                continuar()
                time.sleep(0.2)
                musicaPausada = False

    else:
        musicaParada = True
        pararMusica()
        musicaPausada = False


def volume(volume):
    alterarVolume(volume)

def pausar():
    pausarMusica()

def continuar():
    continuarMusica()

def pararMusica():
    encerrarMusica()