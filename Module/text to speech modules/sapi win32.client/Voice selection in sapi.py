import win32com.client

sapi = win32com.client.Dispatch("SAPI.SpVoice") # Initialize the SAPI object
voices = sapi.GetVoices()  # List all available voices

'''   SAPI has 2 voice, men and femal voice only two variations.
Voice 0: Microsoft David Desktop - English (United States)
Voice 1: Microsoft Zira Desktop - English (United States)
'''
# Set the volume (0 to 100)
sapi.Volume = 100

# Set the speech speed rate (-10 to 10)  
sapi.Rate = 1   # - 10 the slowest and 10 is the fastest rate of speech

print("Available voices:")
for i, voice in enumerate(voices):
    print(f"Voice {i}: {voice.GetDescription()}")

# Choose a specific voice 
sapi.Voice = voices.Item(1) # (the second one in the list, is selected here)

# Speak the text with the selected voice
sapi.Speak("This is a test of the selected speech type.")

