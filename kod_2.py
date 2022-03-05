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