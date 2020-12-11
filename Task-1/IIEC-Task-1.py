import os
import pyttsx3 as pt

pt.speak("Welcome")
print("!!!!Welcome!!!!")
pt.speak("Myself Sammy, I am here to help you.")
pt.speak("Some tasks I can do are - ")
pt.speak("Launching browser and open a website.")
print("1) Chrome")
pt.speak("Open Notebook")
print("2) Notebook")
pt.speak("Open MS Paint")
print("3) MS Paint")
pt.speak("Show your Memories")
print("4) Microsoft Photos")
pt.speak("Setup an Alarm, Timer or Stopwatch")
print("5) Clock")
pt.speak("Help you calculate")
print("6) Calculator")
pt.speak("Capture or Record you")
print("7) Camera")
pt.speak("Make you dance!")
print("8) Music")
pt.speak("Send a mail")
print("9) Gmail")
pt.speak("and lastly Check Weather")
print("10) Weather")
while True:
	pt.speak("Decide one of the above tasks, for me to proceed-")
	s = input()
	if ("exit" in s) or ("quit" in s) or ('break' in s) or ('end' in s) or ('stop' in s) or ('done' in s) or ('none' in s):
		pt.speak('Come again soon.')
		break
	elif ('chrome' in s) or ('browser' in s):
		os.system('chrome')
	elif ('editor' in s) or ('note' in s) or ('notepad' in s) or ('write' in s):
		os.system('notepad')
	elif ('paint' in s) or ('draw' in s):
		os.system('mspaint')
	elif ('photo' in s) or ('image' in s) or ('pic' in s):
		os.system('start ms-photos')
	elif ('clock' in s) or ('time' in s)	or ('stopwatch' in s) or ('alarm' in s):
		os.system('start ms-clock:')
	elif ('calculat' in s) or ('solve' in s):
		os.system('calc')
	elif ('camera' in s) or ('record' in s) or ('capture' in s):
		os.system('start microsoft.windows.camera:')
	elif ('music' in s) or ('listen' in s):
		os.system('vlc')
	elif ('mail' in s) or ('mesaage' in s):
		os.system('chrome gmail.com')
	elif ('weather' in s):
		os.system('start bingweather:')
	else:
		pt.speak('Sorry, no such program available.')