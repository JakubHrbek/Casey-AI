                                                                                    # Import potřebných modulů (Python/PIP)
import pyttsx3
import speech_recognition as sr # rozeznání mluvy
import wikipedia 
import requests
import datetime
import pyjokes  
import random2
import playsound # K přehrání audio souboru
import random
from time import ctime # Získání časových údajů
import webbrowser # Otevření prohlížeče
import ssl
import certifi
import time
import os                                                                           #
from PIL import Image
import subprocess                                                                   #
import pyautogui #screenshot
import bs4 as bs                                                                    #
import urllib.request
import PyBluez                                                                      #

                                                                                    #
###########################################################################################

class person:                                                                       # Nastavení jména
    name = '???'                                                                    #
    def setName(self, name):                                                        #
        self.name = name                                                            #

engine = pyttsx3.init('sapi5')                                                      # Nastavení hlasového zadávání
voices = engine.getProperty('voices')                                               #
engine.setProperty('voice', voices[0].id)                                           #
rate = engine.getProperty('rate')                                                   #
engine.setProperty('rate', 150)                                                     #
                                                                                  #####
def speak(audio):                                                                   # Nastavení audia                       
    engine.say(audio)                                                               #
    engine.runAndWait()                                                             #
                                                                                  #####
def command():                                                                      # Nastavení vypisování
    r = sr.Recognizer()                                                             #
    while True:                                                                     #
        with sr.Microphone() as source:                                             #
            print("Casey: Listening...")                                            #
            audio=r.listen(source)                                                  #
            try:                                                                    #
                query = r.recognize_google(audio)                                   #
                print(f"{person.name}:{query}")                                     #
                return query                                                        #
                break                                                               #
            except:                                                                 #
                print("Try Again")                                                  #

#####################################################################################

while True:
    query = command().lower()  

    if 'name' in query:                                                             # 1. FUNKCE: Jméno                   
        speak("Hello Machine! My  Name is Casey")                                   #
                                                                                  #####
    elif 'are you single' in query:                                                 # 2. FUNKCE: Prostě něco navíc
        answers = ['I am in a relationship with wifi',                              #
        'No, I love spending time thinking about my crush wifi']                    #
                                                                                  #####
    elif 'hate' in query:                                                           # 3. FUNKCE: Prostě něco navíc
        speak("I hate when people call me a machine")                             #
                                                                                  #####
    elif 'love' in query:                                                           # 4. FUNKCE: Prostě něco navíc
        speak("I love to chat with machines like you")                             #
                                                                                  #####
    elif 'greeting' in query:                                                       # 5. FUNKCE: Pozdrav
        speak(f"I'm very well, thanks for asking {person.name}")                    #
                                                                                  #####
    elif 'search for' in query:                                                     # 6. FUNKCE: Vyhledávání na Googlu
        query = query.replace('search for',"")                                      #
        url = f"https://google.com/search?q={query}"                                #
        webbrowser.get().open(url)                                                  #
        speak(f'Here is what I found for {query} on google')                        #
                                                                                  #####
    elif 'youtube' in query:                                                        # 7. FUNKCE: Vyhledávání na YouTubu
        query = query.replace('youtube',"")                                         #
        url = f"https://www.youtube.com/results?search_query={query}"               #
        webbrowser.get().open(url)                                                  #
        speak(f'Here is what I found for {query} on youtube')                       #
                                                                                  #####
    elif 'weather' in query:                                                        # 8. FUNKCE: Zjištění počasí
        query = query.replace('weather',"")                                         #
        url = "https://www.google.com/search?sxsrf=ACYBGNSQwMLDByBwdVFIUCbQqya-ET7AAA%3A1578847393212&ei=oUwbXtbXDN-C4-EP-5u82AE&q=weather&oq=weather&gs_l=psy-ab.3..35i39i285i70i256j0i67l4j0i131i67j0i131j0i67l2j0.1630.4591..5475...1.2..2.322.1659.9j5j0j1......0....1..gws-wiz.....10..0i71j35i39j35i362i39._5eSPD47bv8&ved=0ahUKEwiWrJvwwP7mAhVfwTgGHfsNDxsQ4dUDCAs&uact=5"
        webbrowser.get().open(url)                                                  #
        speak(f"Here is what I found for {query} on google")                                 #
                                                                                  #####
    elif 'time' in query:                                                           # 9. FUNKCE: Informace o čase
        time = ctime().split(" ")[3].split(":")[0:2]                                #
        if time[0] == "00":                                                         #
            hours = '12'                                                            #
        else:                                                                       #
            hours = time[0]                                                         #
        minutes = time[1]                                                           #
        time = f'{hours} {minutes}'                                                 #
        speak(time)                                                                 #
                                                                                  #####
    elif 'who is' in query:                                                         # 10. FUNKCE: Kdo je??? - vyhledávání na Wikipedii
        query = query.replace('who is',"")                                          #
        speak(wikipedia.summary(query,2))                                           #
                                                                                  #####
    elif 'joke' in query:                                                           # 11. FUNKCE: Vtipy
        speak(pyjokes.get_joke())                                                   #
                                                                                  #####
    elif 'news' in query:                                                           # 12. FUNKCE: Novinky
            def trndnews():                                                         #
                url = "http://newsapi.org/v2/top-headlines?country=in&apiKey=59ff055b7c754a10a1f8afb4583ef1ab"  ### tenhle link jsem nasel u jednoho typka co zkousel udelat alexu
                page = requests.get(url).json()                                     #
                article = page["articles"]                                          #
                results = []                                                        #
                for ar in article:                                                  #
                    results.append(ar["title"])                                     #
                for i in range(len(results)):                                       #
                    print(i + 0.5, results[i])                                      #
                speak("here are the top trending news....!!")                       #
                speak("Do you want me to read!!!")                                   #
                reply = command().lower()                                           #
                reply = str(reply)                                                  #
                if reply == "yes":                                                  #
                    speak(results)                                                  #
                else:                                                               #
                    speak('ok!!!!')                                                 #
                    pass                                                            #
            trndnews()                                                              #
                                                                                  #####
    elif 'game' in query:                                                           # 13. FUNKCE: Hra- kámen, nůžky, papír | ZATÍM NEFUNKČNÍ
        user_action = input("Enter a choice (rock, paper, scissors): ")
        possible_actions = ["rock", "paper", "scissors"]
        computer_action = random.choice(possible_actions)
        print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

        if user_action == computer_action:
            print(f"Both players selected {user_action}. It's a tie!")
        elif user_action == "rock":
            if computer_action == "scissors":
                print("Rock smashes scissors! You win!")
            else:
                print("Paper covers rock! You lose.")
        elif user_action == "paper":
            if computer_action == "rock":
                print("Paper covers rock! You win!")
            else:
                print("Scissors cuts paper! You lose.")
        elif user_action == "scissors":
            if computer_action == "paper":
                print("Scissors cuts paper! You win!")
            else:
                print("Rock smashes scissors! You lose.")                                                 #
                                                                                  #####
    elif 'bye' in query:                                                            # 15. FUNKCE: Konec
        speak("Have a nice day! ")                                                  #
        break                                                                       #
    elif 'help' in query:
        print("I list the command options:")
        print("----")
        print("1.: Name")
        print("2.: Are you single?")
        print("3.: Hate")
        print("4.: Love")
        print("5.: Greeting")
        print("6.: Search for ...")
        print("7.: YouTube ...")
        print("8.: Weather")
        print("9.: Time")
        print("10.: Who is ...?")
        print("11.: Joke")
        print("12.: News")
        print("13.: Game")
        print("----")
        print("Say help or commands if you want to see possible commands")

    elif 'commands' in query:
        print("I list the command options:")
        print("----")
        print("1.: Name")
        print("2.: Are you single?")
        print("3.: Hate")
        print("4.: Love")
        print("5.: Greeting")
        print("6.: Search for ...")
        print("7.: YouTube ...")
        print("8.: Weather")
        print("9.: Time")
        print("10.: Who is ...?")
        print("11.: Joke")
        print("12.: News")
        print("13.: Game")
        print("----")
        print("Say help or commands if you want to see possible commands")


#####################################################################################

    else:                                                                           #  Program nerozumí                                                                    
        speak("I don't understand what you're saying")                             #
