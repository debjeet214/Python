import win32com.client

# Initialize the SAPI object
sapi = win32com.client.Dispatch("SAPI.SpVoice")

# Set the volume (0 to 100)
sapi.Volume = 100

# Set the speech rate (-10 to 10)
sapi.Rate = 0  # - 10 the slowest and 10 is the fastest rate of speech

# List available voices
voices = sapi.GetVoices()
for voice in voices:
    print(voice.GetDescription())

# Select a specific voice (e.g., the first one)
sapi.Voice = voices.Item(0)

# Speak the text
sapi.Speak("Hello, this is a test of the SAPI speech engine!"
