import os
import pyautogui
import webbrowser
import pyttsx3
from time import sleep

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)
print(voices[1])  # print want voice you use

def speak(audio):  #ye kese bolega
    engine.say(audio)
    engine.runAndWait()  #bolne ke baad rukhna bhi to he 

dictapp = {"commandprompt":"cmd" , "paint":"paint" , "word":"winword" , "excel":"excel" , "crome" : "crome" , "vscode":"vscode" , "powerpoint":"powerpnt"}

def opnappweb(query):
    speak("launching sir")
    if ".com"in query or ".co.in" in query or ".org" in query:
        query = query.replace("open","")  #query me se open replace kar diya " " space se kar diya
        query = query.replace("zara","") 
        query = query.replace(" ","") 
        query = query.replace("launch","")

        webbrowser.open(f"https://www.{query}")
    else:
        keys=list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"start {dictapp[app]}")
def closeappweb(query):
    speak("closing sir")
    if "one tab" in query or "1 tab "in query:
        pyautogui.hotkey("ctrl","w")
    elif "2 tab" in query :
        pyautogui.hotkey("ctrl","w")
        sleep(0.5) 
        pyautogui.hotkey("ctrl","w")
        speak("all tab close")
    elif "3 tab" in query :
        pyautogui.hotkey("ctrl","w")
        sleep(0.5) 
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("all tab close")
    elif "4 tab" in query :
        pyautogui.hotkey("ctrl","w")
        sleep(0.5) 
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("all tab close")
    elif "5 tab" in query :
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("all tab close")

    else:
        keys=list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"taskkill /f /im {dictapp[app]}.exe")   #jo bhi open karenge vo close bhi kar dega   
    
