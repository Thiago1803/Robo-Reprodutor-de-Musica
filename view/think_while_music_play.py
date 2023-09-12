from view.act_while_music_play import *
from view.act_talk_with_us import *

#MENU COM TRATAMENTO PARA OS COMANDOS QUANDO ESTÁ TOCANDO ALGUMA MUSICA
#A primeira palavra que foi ouvida será o nome do robô e a segunda será o comando
musicaPausada = False

def menuMusicaTocando(textoEntendido):
    comando = textoEntendido[1].lower()
    global musicaPausada
    
    if(comando not in "parar"):
        # Se uma musica estiver tocando, ela será pausada
        if(comando in "pausar"):
            if musicaPausada == False:
                musicaPausada = True
                pausar()
        
        # Se uma musica foi pausada, ela voltara a tocar
        elif(comando in "continuar"):
            if musicaPausada == True:
                musicaPausada = False
                continuar()
                
        else:
            if musicaPausada == False:
                musicaPausada = True
                pausar()

            print("Nao entendi o que você pediu, fale outra vez!")
            
            if musicaPausada == True:
                musicaPausada = False
                continuar()
    else:
        musicaPausada = False
        pararMusica()


def menuParaMensagens(mensagem):
    falarMensagens(mensagem)

def pausar():
    pausarMusica()

def continuar():
    continuarMusica()

def pararMusica():
    encerrarMusica()