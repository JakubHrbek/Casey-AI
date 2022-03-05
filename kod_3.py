def run_Casey():    #tohle asi zmenime UwU
  command = take_Command()
  print(command)
  if 'play' in command:    #zahrat pisnicku
    song = command.replace('play', '')
    talk('playing ' + song)
    pywhatkit.playonyt(song)
  elif 'time' in command:   #toto je pro to kdyz clovek se zepta co je za cas
    time = datetime.datetime.now().strftime('%I:%M %p')   
    talk('Current time is ' + time)
  elif 'who the heck is' in command:    #tohle zas je kdyz clovek se zepta kdo je nekdo napr. kdo je Elon Musk atd.
    person = command.replace('who the heck is', '')
    info
  elif 'date' in command:     #tohle tam nemusi byt (vsechno odsud) je to jen pro srandu ale pokud chcete muzeme nechat
    talk('sorry, I have a headache')
  elif 'are you single' in command:
    talk('I am in a relationship with wifi')
  elif 'joke' in command:
    talk(pyjokes.get_joke())
  else:
    talk('Please say the command again.')
    
while True:
  run_Casey()
