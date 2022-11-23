#importing the modules required.

import pyttsx3
import datetime
import wikipedia
import os
import webbrowser
from googlesearch import *
import speech_recognition as sr


#making a function for voice.
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)     



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#loop for the password.
while True:
    speak("please enter the correct password, to get access to ross")
    password = input("password: ")
    if password == "profile":
        speak("access granted, you are going to use ross")
        print("access granted, you are going to use ross")
        break
    else:
        speak("access denied")
        print("access denied")
        
    


#function , according to this A.I wishes you.   
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning sir ")

    elif hour>=12 and hour<18:
        speak("good afternoon sir ")

    else:
        speak("good evening sir")
    speak("i am ross an Artificial intelligence made by <|name|>. please tell me how may i help you")
    
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.......")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:   {query}\n")

    except Exception as e:
        print(e)

        
        speak("say that again please.....")
        print("say that again please.....")
        return "None"
    return query
    
    
#main function for query.    
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching wikipedia.....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)

        elif "open youtube" in query:
            speak("opening youtube")
            print("opening youtube")
            webbrowser.open("youtube.com")

        elif "hi ross" in query:
            speak("Hi sir, what's app , please tell me what can i do for you")
            print("Hi sir, what's app , please tell me what can i do for you")

        elif "hello ross" in query:
            speak("Hi sir, whatsapp , please tell me what can i do for you")
            print("Hi sir, whatsapp , please tell me what can i do for you")

        elif "hey ross" in query:
            speak("Hi sir, whatsapp , please tell me what can i do for you")
            print("Hi sir, whatsapp , please tell me what can i do for you")

        elif "yourself" in query:
            speak("of course sir")
            print("of course sir")
            speak("i'm ross an artificial intelligence and i am made by ,<|name|> and can do whatever you will say")
            print("i'm ross an artificial intelligence and i am made by ,<|name|> and can do whatever you will say")

        elif "invented" in query:
            speak("<|name|> , invented me")
            print("<|name|> , invented me")
                  
        elif "open rediff" in query:
            speak("opening rediff")
            print("opening rediff")
            webbrowser.open("rediffmail.com")

        elif "central chronicle" in query:
            speak("opening central chronicle")
            print("opening central chronicle")
            webbrowser.open("centralchronicle.com")

        elif "open google" in query:
            speak("opening google")
            print("opening google")
            webbrowser.open("google.com")

        elif "nava bharat" in query:
            speak("opening nava bharat")
            print("opening nava bharat")
            webbrowser.open("navabharat.com")
        
        elif "play music" in query:
            speak("playing music")
            print("playing music")
            music_dir = "E:\\Songs"
            
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print("the time is:",strTime)
            speak(f"sir, the time is {strTime}")

        elif "chrome" in query:
            speak("opening chrome")
            print("opening chrome")
            chrome = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome"
            os.startfile(chrome)

        elif "waterfox" in query:
            speak("opening waterfox")
            print("opening waterfox")
            waterfox = "C:\\Program Files\\Waterfox Current\\waterfox"
            os.startfile(waterfox)

        elif "this pc" in query:
            pc = "E:\\This PC - Shortcut"
            speak("opening This pc")
            os.startfile(pc)


        elif "search" in query:
            query = query.replace("search","")
            google_search = search(query)

            chrome_path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
            for url in search(query, tld="co.in", num=1, stop = 1, pause = 2):
                webbrowser.open("https://google.com/search?q=%s" % query)
                speak("searching google...........")
                speak(google_search)
                print(google_search)

        elif "on youtube" in query:
            query = query.replace("on youtube","")
            youtube_search = search(query)

            for url in search(query, tld="co.in", num=1, stop = 1, pause = 2):
                webbrowser.open("https://youtube.com/search?q=%s" % query)
                speak("searching youtube...........")
                speak(youtube_search)
                print(youtube_search)

        elif "on gaana" in query:
            query = query.replace("on gaana","")
            gaana_search = search(query)

            for url in search(query, tld="co.in", num=1, stop = 1, pause = 2):
                webbrowser.open("https://gaana.com/search?q=%s" % query)
                speak("searching gaana...........")
                speak(gaana_search)
                print(gaana_search) 


        elif "images of" in query:
            query = query.replace("images of","")
            google_search = search(query)

            images_path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
            for url in search(query, tld="co.in", num=1, stop = 1, pause = 2):
                webbrowser.open("https://google.com/search?q=%s" % query)
                speak("searching google...........")
                speak(google_search)
                print(google_search)

        elif "images of" in query:
            query = query.replace("images of","")
            google_search = search(query)

            images_path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
            for url in search(query, tld="co.in", num=1, stop = 1, pause = 2):
                webbrowser.open("https://google.com/search?q=%s" % query)
                speak("searching google...........")
                speak(google_search)
                print(google_search)
        
        elif "exit" in query:
            speak("exiting ross")
            print("exiting ross")
            break
            
        elif "shut down" in query:
            speak("shutting down ross")
            print("shutting down ross")
            break


        
            
            
            
            

            
                
                    
                    
                
                    
            
                
            
            
            

