# SAPI (Speech API) via the win32com.client module in Python is a good option, especially if you are working on a Windows environment and need to leverage the built-in speech capabilities provided by the Windows operating system. SAPI is robust and provides good control over voice settings, such as speed, volume, and voice selection.


import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice") # Initialize the SAPI object

name = ["Debjeet", "Mitali", "Rishav", "Ananya"]   # this is a list of names
for i in name:
    str = " Shout out to "
    speaker.speak(str + i)   # speaking out each name with the string added to it

while 1:   # simply keep the code running
	print("Enter the word you want to speak it out by computer") 
	s = input() 
	speaker.Speak(s) # this will speak what you will write in the prompt
# Calling the Dispatch method of the module which interact with Microsoft Speech SDK to speak the given input from the keyboard 
