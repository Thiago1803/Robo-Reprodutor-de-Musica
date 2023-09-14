from view.act_while_music_play import *
from view.act_talk_with_us import *

#MENU COM TRATAMENTO PARA OS COMANDOS QUANDO ESTÁ TOCANDO ALGUMA MUSICA
#A primeira palavra que foi ouvida será o nome do robô e a segunda será o comando
musicaPausada = False

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
                musicaPausada = False
                continuar()
                
        else:
            print("Nao entendi o que você pediu, fale outra vez!")

    else:
        musicaPausada = False
        pararMusica()


def volume(volume):
    alterarVolume(volume)

def menuParaMensagens(mensagem):
    falarMensagens(mensagem)

def pausar():
    pausarMusica()

def continuar():
    continuarMusica()

def pararMusica():
    encerrarMusica()