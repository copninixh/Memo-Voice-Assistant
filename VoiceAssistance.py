import speech_recognition as sr
from gtts import gTTS
import playsound
import os
from time import gmtime ,  strftime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from time import gmtime ,  strftime

r = sr.Recognizer()

#Set time Center
a = strftime("%H:%M:%S")

#Key in fire base
cred = credentials.Certificate('keyfire/memoproject-f3d6e-firebase-adminsdk-fr0rq-4f172d0cbb.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

users_ref = db.collection(u'medical')
docs = users_ref.stream()


for doc in docs:
    print(u'{} => {}'.format(doc.id, doc.to_dict()))


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


while True:
    command = voice_command_processor()
    print(command)
    execute_voice_command(command)