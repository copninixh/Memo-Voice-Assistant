# coding: utf-8
import requests
import json
import datetime, pytz

tz = pytz.timezone('Asia/Bangkok')

def thai_time():
    now = datetime.datetime.now(tz)
    month_name = 'x มกราคม กุมภาพันธ์ มีนาคม เมษายน พฤษภาคม มิถุนายน กรกฎาคม สิงหาคม กันยายน ตุลาคม พฤศจิกายน ธันวาคม'.split()[now.month]
    thai_year = now.year + 543
    time_str = now.strftime('%H:%M:%S')
    return "วันที่ %d เดือน %s พุทธศักราช %d เวลา %s"%(now.day, month_name, thai_year, time_str)

def news_thai():
    response_news = requests.get("https://newsapi.org/v2/top-headlines?country=th&apiKey=a44bca29c3a244c684e4db74c2869fa2")
    print(response_news.status_code)

    query_news = response_news.json()['articles']

    for t in query_news:
        news_detail = t["title"]

    return news_detail

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

    report_weather = "สภาพอากาศประจำ {} ขณะนี้อุณหภูมิเฉลี่ยอยูที่ {} องศาเซลเซียส อุณหภูมิต่ำสุด {} องศาเซลเซียส อุณหภูมิสูงสุด {} องศาเซลเซียส แรงลมที่ {} เมตรต่อวินาที โดยที่สภาพอากาศภาพรวมวันนี้คือ {}".format(thai_time(),weather_mean,weather_min,weather_max,weather_wind,weather_description)

    return report_weather
    

    

    



            