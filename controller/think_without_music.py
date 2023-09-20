import os
from view.act_start_music import *
from view.act_talk_with_us import *

# Pasta do projeto com as musicas
pasta = "C:/Users/User/Desktop/TRABALHO IA/TRABALHOIA/model/musicas"



#MENU COM TRATAMENTO PARA OS COMANDOS QUANDO NÃO ESTA TOCANDO NENHUMA MUSICA
#A primeira palavra que foi ouvida será o nome do robô e a segunda será o comando
def menuSemMusica(textoEntendido):
    if("desligar" not in textoEntendido and "Desligar" not in textoEntendido):
        # Busca uma determinada musica para reproduzi-la
        if("tocar" in textoEntendido or "Tocar" in textoEntendido):
            textoEntendido = textoEntendido[1:] #ignora "tocar" da lista, sobrando nome do cantor/banda e musica
            buscarMusica(textoEntendido)

        # Reproduz a playlist inteira
        elif("reproduzir" in textoEntendido or "Reproduzir" in textoEntendido):
            reproduzirPlaylist()



# Envia mensagens de erro ou de despedida para o robô falar
def menuParaMensagens(mensagem):
    falarMensagens(mensagem)



# Verifica se a pasta de musicas esta vazia
def verificarPlaylist(pasta):
    if not os.listdir(pasta):
        menuParaMensagens("Playlist sem músicas!")
        return -1
    
    return 1




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
    


def reproduzirPlaylist():   
    if verificarPlaylist(pasta) == 1:
        # Percorre todos os arquivos na pasta, reproduzindo cada musica
        for arquivo in os.listdir(pasta):
            caminho_arquivo = os.path.join(pasta, arquivo)
            tocarMusica(caminho_arquivo)
        