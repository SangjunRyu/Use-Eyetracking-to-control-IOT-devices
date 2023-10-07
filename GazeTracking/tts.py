from gtts import gTTS
import playsound
import os

lang = 'ko'
abs_path = "C:\\Users\\ysjun5656\\Desktop\\eyetracking model\\Eyeverything\\GazeTracking\\TTS"

# text = '입력하고 싶은 내용'
sp = gTTS(lang=lang, text = 'TV 전원', slow = False)
audio = 'TV 전원.mp3'

mp3_path = os.path.join(abs_path, audio)
#sp.save(mp3_path)
playsound.playsound(mp3_path)