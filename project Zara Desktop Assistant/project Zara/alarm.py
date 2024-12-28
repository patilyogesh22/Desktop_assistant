import pyttsx3
import datetime
import os 

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate",200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

extractedtime = open("Alarmtext.txt","rt")  #jo time ham bolenge jo allarm.txt me save ho jayega 
time = extractedtime.read() 
Time = str(time)  # time ki string ko extract karega 
extractedtime.close()

deletetime = open("Alarmtext.txt","r+")  #delete karega time 
deletetime.truncate(0)
deletetime.close()

def ring(time):
    timeset = str(time)
    timenow = timeset.replace("zara","")
    timenow = timenow.replace("set an alarm","")
    timenow = timenow.replace(" and ",":")
    Alarmtime = str(timenow)
    print(Alarmtime)
    while True:
        currenttime = datetime.datetime.now().strftime("%H:%M:%S")
        if currenttime == Alarmtime:
            speak("Alarm ringing,sir")
            os.startfile("music.mp3.wav") 
        elif currenttime + "00:00:20" == Alarmtime:
            exit()   
ring(time)

