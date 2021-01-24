import json
from gtts import gTTS
import playsound
import os

def load_data():
    try: 
        f = open("dict.json")
        json_str = f.read()
        f.close()
        dic_data = json.loads(json_str)
        return dic_data
    except:
        dict = {"สวัสดี": "สวัสดีค่ะ", "คุณคือใคร": "ฉันชื่อ 'เก่งแชทบอท'"}
        js = json.dumps(dict)
        f = open("dict.json","w")
        f.write(js)
        f.close()
        return dict

def addword(data):
    print("ไม่พบประโยคนี้ในระบบ คุณต้องการสอนไหม")
    check = input("Y or N : ")
    if check == 'Y' or check == 'y':
        question = input("คำถาม : ")
        answer = input("คำตอบ : ")
        data[question] = answer
        js = json.dumps(data)
        f = open("dict.json","w")
        f.write(js)
        f.close()

def play_sound(data):
    tts = gTTS(text=data,lang='th')
    tts.save('sound.mp3')
    print(data)
    playsound.playsound('sound.mp3', True)
    os.system('rm sound.mp3')

while True:
    data = load_data()
    text = input("> ")
    if text in data:
        play_sound(data[text])
    else:
        addword(data)