import beepy as beep
import json
from controller.think_music import *
import speech_recognition as sr

def speech_to_text(mensagem):
    # Initialize the recognizer
    recognizer = sr.Recognizer()
    textoNaoEntendido = []

    # Capture audio from the microphone
    with sr.Microphone() as source:
        #print(sr.Microphone.list_microphone_names())
        print(mensagem)
        recognizer.adjust_for_ambient_noise(source)  # Adjust for noise
        audio = recognizer.listen(source)

    try:
        # Recognize the speech using Google Web Speech API
        text = recognizer.recognize_google(audio, language='pt-BR')
        arrText = text.split(' ')
        print("Você falou:", arrText)

        return arrText

    except sr.UnknownValueError:
        print("Robô não identificou nada")
    
    except sr.RequestError as e:
        print("Sorry, an error occurred. Could not request results; {0}".format(e))
    
    return textoNaoEntendido



def menuSentir():
    comando = []

    while("desligar" not in comando and "Desligar" not in comando):
        nomeRobo = speech_to_text("Fale algo, estou aguardando me chamar...")
        if("eva" in nomeRobo or "Eva" in nomeRobo or "ebe" in nomeRobo or "Ebe" in nomeRobo):
            if(verificarMusicaTocando() or verificarMusicaPausada()):
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

            else:
                beep.beep(1)

                comando = speech_to_text("Fale algo, estou ouvindo sem musica tocando...")
                controle = 0

                with open ('./model/dataset.json', 'r') as file:
                    dataset = json.loads(file.read())
                    for palavra in comando:
                        if palavra in dataset['comandosSemMusica']:
                            controle = 1

                        
                if((len(comando)==0) or (controle==0)):
                    beep.beep(3)
                else:
                    menuSemMusica(comando)