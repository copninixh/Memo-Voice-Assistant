import speech_recognition as sr
from gtts import gTTS
import playsound
from time import gmtime ,  strftime
from firebase_admin import credentials
from firebase_admin import firestore
import pafy
import os
os.add_dll_directory(r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\VideoLAN')
import vlc

import youtube_dl

r = sr.Recognizer()




def voice_command_processor():
    with sr.Microphone() as source:
        audio = r.listen(source,phrase_time_limit=4)
        text = ''
        try:
            text =r.recognize_google(audio , language='th')
        except sr.UnknownValueError as e:
            print(e)
        except sr.RequestError as e:
            print("service is down")

        return text.lower()

def music_command():
    with sr.Microphone() as source:
        audio2 = r.listen(source,phrase_time_limit=4)
        textmusic = ''
        try:
            textmusic =r.recognize_google(audio2 , language='th')
        except sr.UnknownValueError as e2:
            print(e2)
        except sr.RequestError as e2:
            print("service is down")

        return textmusic.lower()


def audio_playback(text):
    filename = "text.mp3"
    tts = gTTS(text=text, lang='th')
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

def execute_voice_command(text):
    if "สวัสดี" in  text:
        audio_playback("สวัสดีฉัน Memo")
    elif "Memo ช่วยอะไรได้บ้าง" in text:
        audio_playback("ช่วยเป็นเพื่อนคุยแก้เหงา ช่วยเปิดเพลงที่คุณชอบ ช่วยแจ้งเตือนกินยาค่ะ")
    elif "เปิดเพลง" in text:
        playsound.playsound('02.mp3')
    elif "เล่นเพลง" in text:
        url = "https://www.youtube.com/watch?v=w0GDEgCAsWk&ab_channel=%E0%B8%A1%E0%B8%99%E0%B8%95%E0%B9%8C%E0%B9%81%E0%B8%84%E0%B8%99%E0%B9%81%E0%B8%81%E0%B9%88%E0%B8%99%E0%B8%84%E0%B8%B9%E0%B8%99OFFICIAL"
        video = pafy.new(url)
        best = video.getbest()
        playurl = best.url
        Instance = vlc.Instance()
        player = Instance.media_player_new()
        Media = Instance.media_new(playurl)
        Media.get_mrl()
        player.set_media(Media)
        player.play()
        if "หยุดเพลง" in text:
            player.pause()
        elif "เล่นต่อ" in text:
            player.resume()
        elif "จบเพลง" in text:
            player.stop()


while True:
    command = voice_command_processor()
    print(command)
    execute_voice_command(command)