# coding: utf-8
import speech_recognition as sr
import pygame.mixer
from gtts import gTTS
import playsound
import pafy
import os
os.add_dll_directory(r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\VideoLAN')
import vlc
import requests
import json
import datetime, pytz
from datetime import datetime
import youtube_dl
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from time import sleep , gmtime , strftime
import time
r = sr.Recognizer()
tz = pytz.timezone('Asia/Bangkok')
now = datetime.now(tz)
time_now  = now.strftime("%H:%M")

cred = credentials.Certificate('keyfire/memoproject-f3d6e-firebase-adminsdk-fr0rq-4f172d0cbb.json')
firebase_admin.initialize_app(cred)
db = firestore.client()
listact = []
meee = []
def firebase_activity():
    medical_ref = db.collection(u'activity')
    docs = medical_ref.stream()
    
    for doc in docs:
        act = doc.to_dict()
        val1 = act['start']
        hour,minute,second,tzinfo = val1.hour, val1.minute, val1.second, val1.tzinfo
        utc_time  = "%s:%s"%(hour,minute)
                
        #mytime = datetime.strptime(utc_time,'%H:%M') - datetime.strptime("05:00", "%H:%M")
        mytime = "11:08"
        if(time_now == mytime):
            listact.append(act['actname'])
        else:
            print('2')
            
    return listact

def firebase_medicine():
    medical_refe = db.collection(u'medicine')
    docs_medi = medical_refe.stream()
    
    for medic in docs_medi:
        med = medic.to_dict()
        me = med['namemed']
        for ii in med['medtag']:
            if(ii == 'เช้า'):
                set_time = '01:43'
                if(time_now == set_time):
                    meee.append('ได้เวลากิน{}'.format(me))
                else:
                    print('0')
            else:
                set_time = '02:30'
                if(time_now == set_time):
                    meee.append('ได้เวลากิน{}'.format(me))
                else:
                    print('1')

    return meee

def thai_time():
    now = datetime.datetime.now(tz)
    month_name = 'x มกราคม กุมภาพันธ์ มีนาคม เมษายน พฤษภาคม มิถุนายน กรกฎาคม สิงหาคม กันยายน ตุลาคม พฤศจิกายน ธันวาคม'.split()[now.month]
    thai_year = now.year + 543
    time_str = now.strftime('%H:%M:%S')
    return "วันที่ %d เดือน %s พุทธศักราช %d เวลา %s"%(now.day, month_name, thai_year, time_str)

def news_thai():
    response_news = requests.get("https://newsapi.org/v2/top-headlines?country=th&apiKey=a44bca29c3a244c684e4db74c2869fa2")

    query_news = response_news.json()['articles']

    news_list = []

    for t in query_news:
        news_list.append(t["title"])

    return news_list

def covid19_th():
    response_covid = requests.get("https://coronavirus-19-api.herokuapp.com/countries/thailand")
    query_covid = response_covid.json()
    allcase = query_covid["cases"]
    alldeath = query_covid["deaths"]
    todaycase = query_covid["todayCases"]
    todydeath = query_covid["todayDeaths"]
    recovered = query_covid["recovered"]
    active = query_covid["active"]
    critical = query_covid["critical"]

    allreport = "สถานการณ์โควิดของประเทศไทยจำนวนติดเชื้อสะสมวันนี้ {} คน จำนวนผู้เสียชีวิต {} คน จำนวนผู้รักษาหาย {} คน จำนวนผู้รักษาอยู่ในโรงพยาบาล {} คน จาก จำนวนติดเชื้อสะสม {} คน หายแล้วทั้งหมด {} คน และตายทั้งหมด {} คน ".format(todaycase,todydeath,critical,active,allcase,recovered,alldeath)

    return allreport

def weather():
    response_weather = requests.get("http://api.openweathermap.org/data/2.5/weather?q=Chiang Mai&appid=d7223339fc60fae79adfb6dacb3d12f6&lang=th&units=metric")

    query_weather = response_weather.json()["main"]
    query_wind = response_weather.json()["wind"]
    query_description = response_weather.json()["weather"]

    weather_mean = query_weather["temp"]
    weather_min = query_weather["temp_min"]
    weather_max = query_weather["temp_max"]
    weather_wind = query_wind["speed"]
    for tt in query_description:
        weather_description = tt["description"]

    report_weather = "สภาพอากาศประจำ {} ขณะนี้อุณหภูมิเฉลี่ยอยูที่ {} องศาเซลเซียส อุณหภูมิต่ำสุด {} องศาเซลเซียส อุณหภูมิสูงสุด {} องศาเซลเซียส แรงลมที่ {} เมตรต่อวินาที โดยที่สภาพอากาศภาพรวมวันนี้คือ {} ".format(thai_time(),weather_mean,weather_min,weather_max,weather_wind,weather_description)

    return report_weather



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

#If you use Raspberry PI4 for run this code

# def audio_playback(text):
#     tts = gTTS(text=text, lang='th')
#     tts.save('filename.wav')
#     pygame.mixer.init()
#     path_name=os.path.realpath('filename.wav')
#     real_path=path_name.replace('\\','\\\\')
#     pygame.mixer.music.load(open(real_path,"rb"))
#     pygame.mixer.music.play()
#     while pygame.mixer.music.get_busy():
#         sleep(1)

#If you used Windows for run this code
def audio_playback(text):
    filename = "text.mp3"
    tts = gTTS(text=text, lang='th')
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)




def execute_voice_command(text):
    if "สวัสดี" in  text:
        audio_playback("สวัสดีฉัน Memo ผู้ช่วยของคุณค่ะ")
    elif "ช่วย" in text:
        audio_playback("ช่วยเป็นเพื่อนคุยแก้เหงา ช่วยเปิดเพลงที่คุณชอบ ช่วยแจ้งเตือนกินยาค่ะ")
    elif "เปิดเพลง" in text:
        pygame.mixer.init()
        pygame.mixer_music.load("02.mp3")
        pygame.mixer_music.play()
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
        # if "หยุดเพลง" in text:
        #     player.pause()
        # elif "เล่นต่อ" in text:
        #     player.resume()
        # elif "จบเพลง" in text:
        #     player.stop()
    elif "โควิด" in text:
        audio_playback(covid19_th())
    elif "อากาศ" in text:
        audio_playback(weather())
    elif "ข่าว" in text:
        for news_v in news_thai():
            audio_playback(news_v)
    else:
        for activity_v in firebase_activity():
            audio_playback(activity_v)
            
        for medi_v in firebase_medicine():
            audio_playback(medi_v)
            
   
while True:
    command = voice_command_processor()
    print(command)
    execute_voice_command(command)
   
    
    