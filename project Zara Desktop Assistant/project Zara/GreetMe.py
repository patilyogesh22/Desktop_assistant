import pyttsx3
import datetime

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)

def speak(audio):  #ye kese bolega
    engine.say(audio)
    engine.runAndWait()  #bolne ke baad rukhna bhi to he 

def greetMe():  #automatic time ke according bolega (lakin kese ?)
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("good morning,sir")
    elif hour>12 and hour<=18:
        speak("good afternoon,sir")
    
    else:
        speak("good evening , sir")
    
    
    speak("I am your assistant zara, how can I help you today sir?")

