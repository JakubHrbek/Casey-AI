###Import potřebných modulů (Python/PIP)
import pyttsx3
import speech_recognition as sr
import wikipedia
import requests
import datetime
import pyjokes
import random2
import requests
import os



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)   
    engine.runAndWait()

def command():
    r = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            print("Casey: Listening...")
            audio=r.listen(source)
            try:    
                query = r.recognize_google(audio)
                print(f"master:{query}")
                return query
                break
            except:
                print("Try Again")

while True:
    query = command().lower()  
    
    if 'name' in query:
        speak("Hello Machine! My  Name is Casey")
    elif 'are you single' in query:
        answers = ['I am in a relationship with wifi','No, I love spending time thinking about my crush wifi']
    elif 'hate' in query:
        speak("I hate when people called me a machine")
    elif 'love' in query:
        speak("I loves to chat with machines like you")
    ### cas
    elif 'time' in query:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak("It's {time} master")
    
    ### kdo je...
    elif 'who is' in query:
        query = query.replace('who is',"")
        speak(wikipedia.summary(query,2))
    
    ### vtipy
    elif 'joke' in query:
        speak(pyjokes.get_joke())
    

    ### noviny
    elif 'news' in query:
            def trndnews(): 
                url = "http://newsapi.org/v2/top-headlines?country=in&apiKey=59ff055b7c754a10a1f8afb4583ef1ab"  ### tenhle link jsem nasel u jednoho typka co zkousel udelat alexu
                page = requests.get(url).json() 
                article = page["articles"] 
                results = [] 
                for ar in article: 
                    results.append(ar["title"]) 
                for i in range(len(results)): 
                    print(i + 1, results[i]) 
                speak("here are the top trending news....!!")
                speak("Do yo want me to read!!!")
                reply = command().lower()
                reply = str(reply)
                if reply == "yes":
                    speak(results)
                else:
                    speak('ok!!!!')
                    pass
            trndnews() 


  
    ### hudba
    elif 'music' in query:

        music_dir = '\music'
        songs = os.listdir(music_dir)
        song = random2.randint(0,len(songs)-1)
        print(songs[song])  
        speak(f"playing{songs[song]}")
        os.startfile(os.path.join(music_dir, songs[0]))

    elif "bye" in query:
        speak("Have a nice day ! ")
        break
    elif "end" in query:
        speak("Have a nice day ! ")
        break
    elif "exit" in query:
        speak("Have a nice day ! ")
        break
    elif "bye" in query:
        speak("Have a nice day ! ")
        break
    else:
        speak("I don't understand what you are saying")
