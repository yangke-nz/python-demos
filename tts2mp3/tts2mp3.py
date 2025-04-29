import pyttsx3
import os
from pydub import AudioSegment
from pathlib import Path

engine = pyttsx3.init()

in_file = 'textfile'
script_dir = Path(__file__).parent.resolve()
output_path = script_dir / f"{in_file}_voice.wav" 


#engine.setProperty('rate', 180)
#engine.setProperty('voice', 'com.apple.speech.synthesis.voice.tessa') 
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) 
# engine.say(text) 
# engine.runAndWait()


with open(str(script_dir)+'./'+ in_file +'.txt', 'r', encoding='utf-8') as file: 
    text = file.read()
    
engine.save_to_file(text, str(output_path)) 
# engine.say(text) 
engine.runAndWait()


# Convert to MP3 using pydub (require ffmpeg)
mp3_path = script_dir / f"{in_file}_voice.mp3" 
AudioSegment.from_wav(str(output_path)).export(mp3_path, format="mp3", bitrate="96k", codec="libmp3lame", parameters=["-ar", "22050", "-ac", "1"] )


os.remove(output_path)