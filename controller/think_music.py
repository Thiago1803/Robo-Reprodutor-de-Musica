import os
import threading
import time
from view.act_music import *
from view.act_talk import *

# Pasta do projeto com as musicas
pasta = "C:/Users/ricar/Documents/cpp/periodo 6/ia/TRABALHOIA/model/musicas"
pastaPlaylistInfantil = "C:/Users/ricar/Documents/cpp/periodo 6/ia/TRABALHOIA/model/playlist infantil"
pastaPlaylistFesta = "C:/Users/ricar/Documents/cpp/periodo 6/ia/TRABALHOIA/model/playlist festa"
pastaPlaylistTriste = "C:/Users/ricar/Documents/cpp/periodo 6/ia/TRABALHOIA/model/playlist triste"
musicaPausada = False


# Envia mensagens de erro ou de despedida para o robô falar
def menuParaMensagens(mensagem):
    falarMensagens(mensagem)


# Verifica se a pasta de musicas esta vazia
def verificarPlaylist(pasta):
    if not os.listdir(pasta):
        menuParaMensagens("Playlist sem músicas!")
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
    if("desligar" not in textoEntendido and "Desligar" not in textoEntendido):
        # Busca uma determinada musica para reproduzi-la
        if("tocar" in textoEntendido or "Tocar" in textoEntendido):
            textoEntendido = textoEntendido[1:] #ignora "tocar" da lista, sobrando nome do cantor/banda e musica
            separator = '' #indica como irá separar as palavras da lista, no caso é sem espaço
            musica = [separator.join(textoEntendido)] #concatena todas as palavras da lista
            buscarMusica(musica)

        # Reproduz a playlist infantil
        elif("reproduzir playlist infantil" in textoEntendido or "infantil" in textoEntendido):
            threading.Thread(target=reproduzirPlaylist, args=(pastaPlaylistInfantil,)).start()  # Passar a pasta como argumento

        # Reproduz a playlist festa
        elif("reproduzir playlist festa" in textoEntendido or "festa" in textoEntendido):
            threading.Thread(target=reproduzirPlaylist, args=(pastaPlaylistFesta,)).start()  # Passar a pasta como argumento

        # Reproduz a playlist triste
        elif("reproduzir playlist triste" in textoEntendido or "triste" in textoEntendido):
            threading.Thread(target=reproduzirPlaylist, args=(pastaPlaylistTriste,)).start()  # Passar a pasta como argumento
    else:
        menuParaMensagens("Desligando... Até mais!")

    

def buscarMusica(nome):
    if verificarPlaylist(pasta) == 1:
        #Variavel de controle para indicar se a musica foi encontrada ou nao
        musicaIniciou = False

        # Percorre todos os arquivos na pasta, reproduzindo a musica desejada caso for encontrada
        for arquivo in os.listdir(pasta):
            caminho_arquivo = os.path.join(pasta, arquivo)
            nome_arquivo, extensao= os.path.splitext(caminho_arquivo)

            # Transforma ambas strings em palavras com letras minusculas e compara se existe um arquivo com o nome informado
            if nome[0].lower() in nome_arquivo.lower():
                tocarMusica(caminho_arquivo)
                musicaIniciou = True
        
        if(musicaIniciou == False):
            menuParaMensagens("Música nao encontrada!")
        else:
            musicaIniciou = False
    

def reproduzirPlaylist(pasta):

    global pastaPlaylistAtual  # Atualizando a variável global
    pastaPlaylistAtual = pasta

    if verificarPlaylist(pasta) == 1:
        # Percorre todos os arquivos na pasta, reproduzindo cada musica
        for arquivo in os.listdir(pasta):
            caminho_arquivo = os.path.join(pasta, arquivo)
            tocarMusica(caminho_arquivo)
            while(verificarMusicaTocando() or verificarMusicaPausada()):
                continue

def menuMusicaTocando(textoEntendido):
    global musicaPausada
    
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
        
        elif("pular" not in textoEntendido and "Pular" not in textoEntendido):
               if musicaPausada == False:
                pularMusica(pastaPlaylistAtual)

    else:
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