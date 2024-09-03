import pyttsx3
import speech_recognition as sr
import datetime


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print (voices)
#print (voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
       speak("Good afternoon!")

    else:
       speak("Good Evening!")

    speak("I am friday. please tell me how may I help you")

def takeCommand():
    #IT takes microphone input from the user and return string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    new_func(r, audio)

def new_func(r, audio):
    
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')

       



if __name__ == "__main__":
    wishMe()



