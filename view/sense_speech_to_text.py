import speech_recognition as sr

def speech_to_text(mensagem):
    # Initialize the recognizer
    recognizer = sr.Recognizer()
    textoNaoEntendido = []

    # Capture audio from the microphone
    with sr.Microphone() as source:
        print(sr.Microphone.list_microphone_names())
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