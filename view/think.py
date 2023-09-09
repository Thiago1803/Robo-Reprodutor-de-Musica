import os
from view.act import *

# Pasta do projeto com as musicas
pasta = "/home/thiago/Área de Trabalho/TRABALHOIA/musicas"



#MENU COM TRATAMENTO PARA OS COMANDOS QUANDO NÃO ESTA TOCANDO NENHUMA MUSICA
#A primeira palavra que foi ouvida será o nome do robô e a segunda será o comando

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
            falarMensagens ("Até mais...")
    else:
        falarMensagens ("Está tentando falar comigo? Me chame pelo nome!")




#MENU COM TRATAMENTO PARA OS COMANDOS QUANDO ESTÁ TOCANDO ALGUMA MUSICA
#A primeira palavra que foi ouvida será o nome do robô e a segunda será o comando

def menuMusicaTocando(textoEntendido):
    musicaTocando = True

    if(textoEntendido[0].lower() in "robô"):
        if(textoEntendido[1].lower() not in "parar"):
            # Pausa a musica que esta tocando
            if(textoEntendido[1].lower() in "pausar"):
                if musicaTocando == True:
                    musicaTocando = False
                    pausar()
            
            # Volta a reproduzir a musica que foi pausada
            elif(textoEntendido[1].lower() in "continuar"):
                if musicaTocando == False:
                    musicaTocando = True
                    continuar(musicaTocando)
                    
            else:
                pausar()
                falarMensagens ("Nao entendi o que você pediu, fale outra vez!")
                continuar()
        else:
            musicaTocando = False
            pararMusica()




#MUSICA
def pausar():
    pausarMusica()

def continuar():
    continuarMusica()

def pararMusica():
    encerrarMusica()


def buscarMusica(nome):
    # Verifica se a pasta de musicas esta vazia
    if not os.listdir(pasta):
        falarMensagens("Playlist sem músicas!")
    
    # Percorre todos os arquivos na pasta, reproduzindo a musica desejada caso for encontrada
    else:
        #Variavel de controle para indicar se a musica foi encontrada ou nao
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
    # Verifica se a pasta de musicas esta vazia
    if not os.listdir(pasta):
        falarMensagens("Playlist sem músicas!")

    # Percorre todos os arquivos na pasta, reproduzindo cada musica
    else:
        for arquivo in os.listdir(pasta):
            caminho_arquivo = os.path.join(pasta, arquivo)
            tocarMusica(caminho_arquivo)




#DANÇA