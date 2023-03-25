import pyttsx3
engine = pyttsx3.init()


engine.setProperty('rate', 180)
#engine.setProperty('voice', 'com.apple.speech.synthesis.voice.tessa') 
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id) 
text = 'Pyttsx3 is a Python library for converting text to speech, and it differs from other libraries in that it functions without requiring an internet connection.'

engine.say(text) 
engine.runAndWait()

engine.save_to_file(text, 'output_voice.mp3') 
engine.runAndWait()
