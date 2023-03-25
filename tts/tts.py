import pyttsx3
engine = pyttsx3.init()


engine.setProperty('rate', 180)
engine.setProperty('voice', 'com.apple.speech.synthesis.voice.tessa') 

text = 'Pyttsx3 is a Python library for converting text to speech, and it differs from other libraries in that it functions without requiring an internet connection.'

engine.say(text) 
engine.runAndWait()

#engine.save_to_file(text, 'test.wav') engine.runAndWait()
