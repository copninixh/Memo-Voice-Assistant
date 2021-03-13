import pygame.mixer
import speech_recognition as sr
from gtts import gTTS
import pyaudio
import os
from time import sleep , gmtime , strftime
import RPi.GPIO as GPIO
import time
import json
r = sr.Recognizer()

GPIO.setmode(GPIO.BCM)

PIR_PIN = 4

GPIO.setup(PIR_PIN, GPIO.IN)


try:
    print("start")
    time.sleep(2)
    print("Ready")
    while True:
        if GPIO.input(PIR_PIN):
            print("Detect Object 6m 120 radius ")
            pygame.mixer.init()
            pygame.mixer_music.load("/home/pi/Desktop/Raspberry PI_MEMO/noti.mp3")
            pygame.mixer_music.play()

            while pygame.mixer_music.get_busy() == True:
                continue

            def voice_command_processor():
                with sr.Microphone() as source:
                    audio = r.listen(source,phrase_time_limit=4)
                    text = ''
                    try:
                        text =r.recognize_google(audio ,language='th')
                    except sr.UnknownValueError as e:
                        print(e)
                    except sr.RequestError as e:
                        
                        print("service is down")

                    return text.lower()

            def audio_playback(text):
                tts = gTTS(text=text, lang='th')
                tts.save('filename.wav')
                pygame.mixer.init()
                path_name=os.path.realpath('filename.wav')
                real_path=path_name.replace('\\','\\\\')
                pygame.mixer.music.load(open(real_path,"rb"))
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy():
                    sleep(1)

            def excute_voice_command(text):
                if "สวัสดี" in text:
                    audio_playback("สวัสดี ฉัน MEMO ผู้ช่วยของคุณมีอะไรให้ฉันช่วยไหมคะ")
                elif "ฉันคือใคร" in text:
                    audio_playback("ค้าย")
                elif "เปิดเพลง" in text:
                    pygame.mixer.init()
                    pygame.mixer_music.load("/home/pi/Desktop/Raspberry PI_MEMO/pee.mp3")
                    pygame.mixer_music.play()
                elif "กินยา" in text:
                    audio_playback("กำลงตรวจสอบ")
                    audio_playback("ช่วงหลังอาหารเช้า 9 โมง ครึ่ง")
                    audio_playback("ยาแก้ปวด ลักษณะ เม็ดสีขาวกลม")
                elif "เบอร์โทร" in text:
                    audio_playback("นี่คือเบอร์โทรของคนใกล้ชิด 089-988-6589")
                else:
                    audio_playback("สวัสดี ฉัน MEMO ผู้ช่วยของคุณมีอะไรให้ฉันช่วยไหมคะ")


            while True:
                command = voice_command_processor()
                print(command)
                excute_voice_command(command)

except KeyboardInterrupt:
    print("q")
    GPIO.cleanup()




