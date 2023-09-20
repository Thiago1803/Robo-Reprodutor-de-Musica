import beepy as beep
import json
from view.sense_speech_to_text import speech_to_text
from controller.think_while_music_play import menuMusicaTocando
from controller.think_while_music_play import volume

def menuSentir():
    comando = []

    while("parar" not in comando and "Parar" not in comando):
        nomeRobo = speech_to_text("Fale algo, estou ouvindo com a musica tocando...")
        if("beto" in nomeRobo or "Beto" in nomeRobo):
            volume(0.2)
            beep.beep(1)

            comando = speech_to_text("Fale algo, estou ouvindo com a musica tocando...")
            controle = 0
            
            with open ('./model/dataset.json', 'r') as file:
                dataset = json.loads(file.read())
                for palavra in comando:
                    if palavra in dataset['comandosMusicaTocando']:
                        controle = 1

                    
            if((len(comando)==0) or (controle==0)):
                beep.beep(3)
            else:
                menuMusicaTocando(comando)

            volume(1.0)