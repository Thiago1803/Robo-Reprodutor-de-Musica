import speech_recognition as sr
from view.think import menuSemMusica
from view.think import menuMusicaTocando

def speech_to_text():
    pararPrograma = False
    while(pararPrograma == False):
        # Initialize the recognizer
        recognizer = sr.Recognizer()

        # Capture audio from the microphone
        with sr.Microphone() as source:
            print(sr.Microphone.list_microphone_names())
            print("Fale algo...")
            recognizer.adjust_for_ambient_noise(source)  # Adjust for noise
            audio = recognizer.listen(source)

        try:
            # Recognize the speech using Google Web Speech API
            text = recognizer.recognize_google(audio, language='pt-BR')
            arrText = text.split(' ')
            print("Você falou:", arrText)
            if "desligar" in arrText:
                pararPrograma = True
            else:
                menuSemMusica(arrText)
            
        except sr.UnknownValueError:
            menuSemMusica("Nao entendi o que foi dito")
        
        except sr.RequestError as e:
            print("Sorry, an error occurred. Could not request results; {0}".format(e))



def musicaToca():
    pararPrograma = False
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Capture audio from the microphone
    with sr.Microphone() as source:
        print(sr.Microphone.list_microphone_names())
        print("Fale algo...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for noise
        audio = recognizer.listen(source)

    try:
        # Recognize the speech using Google Web Speech API
        text = recognizer.recognize_google(audio, language='pt-BR')
        arrText = text.split(' ')
        print("Você falou:", arrText)
        menuMusicaTocando(arrText)
        
    except sr.UnknownValueError:
        menuMusicaTocando("Nao entendi o que foi dito")
    
    except sr.RequestError as e:
        print("Sorry, an error occurred. Could not request results; {0}".format(e))