import beepy as beep
from view.think_without_music import menuSemMusica
from view.act_talk_with_us import falarMensagens
from view.sense_speech_to_text import speech_to_text

def menuSentir():
    comando = []

    while("desligar" not in comando and "Desligar" not in comando):
        nomeRobo = speech_to_text("Fale algo, estou ouvindo sem musica tocando...")
        if("beto" in nomeRobo or "Beto" in nomeRobo):
            beep.beep(1)

            comando = speech_to_text("Fale algo, estou ouvindo sem musica tocando...")

            if(len(comando) != 0):
                menuSemMusica(comando)
            else:
                falarMensagens("Nada foi dito.")
    
    beep.beep(3)
