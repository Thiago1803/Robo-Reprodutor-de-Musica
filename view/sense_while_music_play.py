import beepy as beep
from view.sense_speech_to_text import speech_to_text
from view.think_while_music_play import menuMusicaTocando
from view.think_while_music_play import volume

def menuSentir():
    comando = []

    while("parar" not in comando and "Parar" not in comando):
        nomeRobo = speech_to_text("Fale algo, estou ouvindo com a musica tocando...")
        if("beto" in nomeRobo or "Beto" in nomeRobo):
            volume(0.2)
            beep.beep(1)

            comando = speech_to_text("Fale algo, estou ouvindo com a musica tocando...")
            
            if(len(comando) != 0):
                menuMusicaTocando(comando)
            else:
                print("Nada foi dito.")

            volume(1.0)
            