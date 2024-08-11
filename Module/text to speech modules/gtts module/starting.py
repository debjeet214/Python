from gtts import gTTS
import os

mytext = input("enter the speech you want to listen: ")   # inserting what we want to listen
language = 'en'                                           # setting the language to english

output = gTTS(text = mytext, lang = language, slow = False) # taking the output in variable 

output.save("output.mp3")                                   # saing the output in a mp3 file set

os.system("start output.mp3")                               # start reading the new made mp3 file
