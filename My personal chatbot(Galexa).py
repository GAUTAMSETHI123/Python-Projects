import os
import pyttsx3
import speech_recognition as sr
engine=pyttsx3.init()
sound = engine.getProperty('voices')
engine.setProperty('voice',sound[1].id)
pyttsx3.speak("hello master gautam...i am galexa")
pyttsx3.speak("how are you doing today...")
while True:
    variable = sr.Recognizer()
    with sr.Microphone() as source:
        print('How may I help you?')
        engine.runAndWait()
        audio_input = variable.record(source,duration=6)
        try:
            text = variable.recognize_google(audio_input)
            print(text)
        except:
            print('Could not process audio...')
            pyttsx3.speak('Could not process audio')
            break
    if('what' in text) and ('can' in text) and('you' in text) and ('do' in text):
        print(" i can open chrome")
        pyttsx3.speak("i can open chrome ")
        print(" i can open wikipedia")
        pyttsx3.speak("i can open wikipedia ")
        print(" i can open facebook")
        pyttsx3.speak("i can open facebook ")
        print(" i can open whatsapp")
        pyttsx3.speak("i can open whatsapp ")
        print(" i can open youtube")
        pyttsx3.speak("i can open youtube ")
        print(" i can open instagram")
        pyttsx3.speak("i can open instagram ")
        print(" i can open github")
        pyttsx3.speak("i can open github")

    elif ('open' in text)and ('Chrome' in text):
         print("opening chrome")
         pyttsx3.speak("opening chrome")
         os.system("start chrome")


    elif ('open' in text)and ('Wikipedia' in text):
         print("opening wikipedia")
         pyttsx3.speak("opening wikipedia")
         os.system("start chrome https://www.wikipedia.org/")


    elif ('open' in text)and ('Facebook' in text):
         print("opening facebook")
         pyttsx3.speak("opening facebook")
         os.system("start chrome https://www.facebook.com/ ")

    elif (('open' in text)or ('Open' in text))and (('WhatsApp' in text)or('whatsApp' in text)):
         print("opening whatsapp")
         pyttsx3.speak("opening whatsapp")
         os.system("start chrome https://web.whatsapp.com/ ")



    elif (('open' in text)or('Open' in text)) and('YouTube'in text):
         print("opening youtube")
         pyttsx3.speak("opening youtube")
         os.system("start chrome https://www.youtube.com/")


    elif ('open' in text)and ('GitHub' in text):
         print("opening github")
         pyttsx3.speak("opening github")
         os.system("start https://github.com/PipedreamHQ/pipedream/blob/master/components/github/readme.md?gclid=Cj0KCQjwp4j6BRCRARIsAGq4yMG6BwEQN7tOV2EDGZbWzK-xFllVHxh9qq1zAgfO4Qp-BCTaY8Y7-DoaAjRzEALw_wcB ")


    elif ('open' in text)and ('Instagram' in text):
         print("opening Instagram")
         pyttsx3.speak("opening instagram")
         os.system("start chrome https://www.instagram.com/")

         

    elif ("exit" in text)  or ("quit" in text) or ('Exit' in text) or ('Quit' in text):
        print('Bye Bye, have a nice day!!')
        pyttsx3.speak('Bye Bye Have a nice day')
        break
    

        
    else:
        print("command does not support")
        pyttsx3.speak('Command does not support')

