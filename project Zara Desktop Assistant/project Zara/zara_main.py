import pyttsx3
import speech_recognition
import pyaudio
import bs4   
import requests #for requests
from bs4 import BeautifulSoup
import datetime
import os
import pyautogui  #The pyautogui library simulates keyboard and mouse actions.
import speedtest
from INTRO import play_gif
play_gif

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)
print(voices[1])  # print want voice you use

def speak(audio):  #ye kese bolega
    engine.say(audio)
    engine.runAndWait()  #bolne ke baad rukhna bhi to he 

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("listening......")
        r.pause_threshold =1     
        r.energy_threshold=300   #small value low vol. me bolna hoga high kar diya to loud bolna hoga esliye moderate value rakho
        audio = r.listen(source,0,4)  #0,4 - litna time tak vo wait karega (4sec wait phir move kar jayega )
        
    try:
        print("understand..")
        query=r.recognize_google(audio,language='en-in')
        print(f"you said:  {query}\n")
    except Exception as e:
        print("say that again")
        return "None"
    return query

def alarm(query):
    timehere = open("Alarmtext.txt","a")  #This line opens the file Alarmtext.txt in append mode ("a"). Append mode ensures that any new query data is added to the end of the file without overwriting existing content. timehere is the file object for Alarmtext.txt, enabling read/write operations.
    timehere.write(query) #This writes the content of query
    timehere.close()    #  This closes the file after writing to it. Closing the file is good practice to ensure that all data is written and resources are freed.
    os.startfile("alarm.py") #This line uses the os.startfile() function to open (or execute) a file. Here, it attempts to run a script called alarm.py

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if"wake up" in query:        # GreetM.py me jao aur geetme fun. call karo
            from GreetMe import greetMe
            greetMe()

            while True:
                query=takeCommand().lower()
                if "go to sleep" in query:   # sabh sunega lakin execute nhi karega 
                    speak("as you wish sir , call me anytime")  # file band jayegi and resuse ke liya vapis se "wake up"bolna hoga 
                    break 

                elif "hello" in query:  #** ye me bolunga 
                    speak("greeding sir, how are you feeling today")  #** ye system bolenga
                elif "i am fine" in query:
                    speak(" glad to hear , sir")
                elif "how are you" in query: 
                    speak(" i am well  , sir , thanks for asking")
                elif "thank you" in query:
                    speak("its my honor,sir")

                elif "pause" in query : #youtube control
                    pyautogui.press("k") #pyautogui.press("k") simulates pressing the "k" key on the keyboard, which, in many video players (like YouTube), pauses or plays the video.
                    speak("video paused") #speak("video paused"): This line calls the speak() function to convert the text "video paused" to speech, so the program audibly confirms that the video has been paused.
                elif "play" in query:
                    pyautogui.press("k")
                    speak("video played")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted")
                elif "volume up" in query:
                    from keyboard import volumeup
                    speak("Turning volume up,sir")
                    volumeup()
                elif "volume down" in query:
                    from keyboard import volumedown
                    speak("Turning volume down, sir")
                    volumedown()

                #open any app easily ("1 windows option par jayega , 2 search bar par query dalega , 3 open kar dega "(control the keyvoard))
                elif "open" in query:
                    query = query.replace("open","")
                    query = query.replace("zara","")
                    pyautogui.press("super") #pyautogui.press("super"): This line simulates pressing the Windows key on the keyboard,
                    pyautogui.typewrite(query)
                    pyautogui.sleep(2)
                    pyautogui.press("enter") 

                elif "open" in query:  #open any app
                    from Dictapp import opnappweb  #ye dictapp me jayega openappweb funtion ko le ayega
                    opnappweb(query)
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)

                # googgle search 
                elif "google " in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)
                
                elif "temperature" in query:
                    search = "temperature in delhi"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")  #text lakar de denga 
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")
                elif "weather" in query:
                    search = "temperature in delhi"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")

                elif "set an alarm" in query:
                    print("input time example:- 10 and 10 and 10")
                    speak("set the time")
                    a=input("please tell the time")
                    alarm(a)
                    speak("going to sleep ,sir")
                    exit()

                elif "the time "in query :
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"sir , the time is {strTime}")
                
                elif "finally sleep" in query:
                    speak("going to sleep")   # go to sleep - it lissten everything but not respond (for respond you say- wake up)
                    exit()                      # in finaaly sleep it terminates the code not responding and not listtening anything
                
                # remeber funtion
                elif "remember that" in query:
                    rememberMessage = query.replace("remember that","")
                    rememberMessage = query.replace("zara","")
                    speak("You told me to remember that"+rememberMessage)
                    remember = open("Remember.txt","w")
                    remember.write(rememberMessage)
                    remember.close()                   
                elif "what do you remember" in query:
                    remember = open("Remember.txt","r")
                    speak("You told me to remember that" + remember.read())

                #shutdown the system
                elif "shutdown the system" in query:
                    speak("Are You sure you want to shutdown")
                    shutdown = input("Do you wish to shutdown your computer? (yes/no)")
                    if shutdown.lower() == "yes":
                        os.system("shutdown /s /t 1") #/s flag is used to shutdown the system
                    elif shutdown.lower() == "no":
                        speak("shutdown cancel")
                        break

                elif "restart the system" in query:
                    speak("Are You sure you want to restart")
                    restart = input("shutdown your system? (yes/no)")
                    if restart.lower() == "yes":
                        os.system("restart /r /t 1")  #/r flag is used to restart the system 
                    elif restart.lower() == "no":    # /1 sets a 1-second delay before the restart
                        break
                
                #speed test
                elif "internet speed" in query:
                    wifi  = speedtest.Speedtest()
                    upload_net = wifi.upload()/1048576   #Megabyte = 1024*1024 Bytes
                    download_net = wifi.download()/1048576  #not give acctual answer 
                    print("Wifi Upload Speed is", upload_net)
                    print("Wifi download speed is ",download_net)
                    speak(f"Wifi download speed is {download_net}")
                    speak(f"Wifi Upload speed is {upload_net}")            
                
                #screenshot
                elif "screenshot" in query:
                     import pyautogui 
                     im = pyautogui.screenshot()
                     im.save("ss.jpg")
                
                #camera photo
                elif "click my photo" in query:
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    speak("SMILE")
                    pyautogui.press("enter")
                
                #translator
                elif "translate" in query:
                    from Translator import translategl
                    query = query.replace("zara","")
                    query = query.replace("translate","")
                    translategl(query)


                



