import beepy as beep
import json
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
            controle = 0

            with open ('./model/dataset.json', 'r') as file:
                dataset = json.loads(file.read())
                for palavra in comando:
                    if palavra in dataset['comandos']:
                        controle = 1

                    
            if((len(comando)==0) or (controle==0)):
                beep.beep(3)
            else:
                menuSemMusica(comando)
                
    
    falarMensagens("Desligando... Até mais!")
