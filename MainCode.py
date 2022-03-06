import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
  engine.say(text)
  engine.runAndWait()

nevimCoTuMaByt = wikipedia.summary(person, 1)
print(info)
talk(info)def take_command():
try:
        with sr.Microphone() as source:
                print('listening...')
                voice = listener.listen(source)
                command = listener.recognize_google(voice)
                command = command.lower()
                if 'jmeno našeho Home AI' in command:
                        command = command.replace('jmeno našeho Home AI', '')
                        print(command)
except:
        pass
return command


def run_Casey():  # tohle asi zmenime UwU
    command = take_Command()
    print(command)
    if 'play' in command:  # zahrat pisnicku
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:  # toto je pro to kdyz clovek se zepta co je za cas
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who the heck is' in command:  # tohle zas je kdyz clovek se zepta kdo je nekdo napr. kdo je Elon Musk atd.
        person = command.replace('who the heck is', '')
        info
    elif 'date' in command:  # tohle tam nemusi byt (vsechno odsud) je to jen pro srandu ale pokud chcete muzeme nechat
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again.')


while True:
    run_Casey()