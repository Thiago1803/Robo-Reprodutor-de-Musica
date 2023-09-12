import speech_recognition as sr
from view.think_while_music_play import menuMusicaTocando
from view.think_while_music_play import menuParaMensagens

pararMusica = False

def ouvirComMusica():
    global pararMusica
    while(pararMusica == False):
        # Initialize the recognizer
        recognizer = sr.Recognizer()

        # Capture audio from the microphone
        with sr.Microphone() as source:
            print(sr.Microphone.list_microphone_names())
            print("Fale algo, estou ouvindo com a musica tocando...")
            recognizer.adjust_for_ambient_noise(source)  # Adjust for noise
            audio = recognizer.listen(source)

        try:
            # Recognize the speech using Google Web Speech API
            text = recognizer.recognize_google(audio, language='pt-BR')
            arrText = text.split(' ')
            print("Você falou:", arrText)

            if arrText[0].lower() in "papel":
                if arrText[1].lower() in "parar":
                    pararMusica = True
                menuMusicaTocando(arrText)
            else:
                print("Está tentando falar comigo? Me chame pelo nome!")
            
            
        except sr.UnknownValueError:
            print("Nao entendi o que foi dito")
        
        except sr.RequestError as e:
            print("Sorry, an error occurred. Could not request results; {0}".format(e))
    
    pararMusica = False