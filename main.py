import sys
from bs4 import BeautifulSoup
import requests
import json
import discord
import datetime
import jpholiday

#Bot TOKEN
TOKEN = ''
#CHANNEL ID
CHANNNEL = "" 

client = discord.Client()

dayofweek = ['日曜日','月曜日','火曜日','水曜日','木曜日','金曜日','土曜日']

# 起動時に動作する処理
@client.event
async def on_ready():
    print('complete set up.')
    await client.wait_until_ready()
    channel = client.get_channel(int(CHANNNEL))
    await channel.send("```おはよう！```")
    # 起動したらターミナルにログイン通知が表示される
    now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
    marume = now.strftime('%Y年%m月%d日')
    weekday = now.strftime('%w')
    week = dayofweek[int(weekday)]
    ato = datetime.date(now.year,now.month,now.day)
    outdayly = (marume+"  ("+week+")")
    holy = ""
    sendy = ""
    if jpholiday.is_holiday(ato) == True:
        holy = jpholiday.is_holiday_name(ato)
        sendy = "今日は{}だよ！".format(holy)
        print(sendy)
    else:
        if weekday == "6" or weekday == "0":
            sendy = "今日は休日です。ごゆっくりどうぞ！"
        else:
            sendy = "今日も一日頑張りましょう！"
    print("ON")                
    #weather
    city = "Osaka"#your City
    key = ''#Open Weather map API key {https://openweathermap.org/}
    url = "http://api.openweathermap.org/data/2.5/forecast?&q="+city+",JP&units=metric&lang=ja&cnt=7&APPID="+ key

    get_deta = requests.get(url)

    w_deta = get_deta.json()
    jsontxt = json.dumps(w_deta,indent=4)

    j_data = json.loads(get_deta.text)

    print(j_data)

    time=[]
    puts=[]
    humidity=[]
    min_tmp=[]
    max_tmp=[]


    for cnt in range(len(j_data["list"])):
        print(len(j_data["list"]))
        time.append(j_data["list"][cnt]["dt_txt"])
        icon=(j_data["list"][cnt]["weather"][0]["icon"])
        humidity.append(j_data["list"][cnt]["main"]["humidity"])
        min_tmp.append(j_data["list"][cnt]["main"]["temp_min"])
        max_tmp.append(j_data["list"][cnt]["main"]["temp_max"])

        if(icon == "01d" or icon == "01n"):
            puts.append("快晴")
        elif(icon == "02d" or icon == "02n"):
            puts.append("晴れ")
        elif(icon == "03d" or icon == "04d" or icon == "03n" or icon == "04n"):
            puts.append("くもり")
        elif(icon == "09d" or icon == "09n"):
            puts.append("小雨")
        elif(icon == "10d" or icon == "10n"):
            puts.append("雨")
        elif(icon == "11d" or icon == "11n"):
            puts.append("雷雨")
        elif(icon == "13d" or icon == "13n"):
            puts.append("雪")
        elif(icon == "50d" or icon == "50n"):
            puts.append("霧")

    out_weather = discord.Embed(title = "今日の大阪府の天気！",color = discord.Colour.from_rgb(18,207,224))
    out_weather.add_field(name = outdayly, value = sendy,inline=False)
    #tenki
    out_weather.add_field(name = "03:00",value = puts[0],inline=True)
    out_weather.add_field(name = "06:00",value = puts[1],inline=True)
    out_weather.add_field(name = "09:00",value = puts[2],inline=True)
    out_weather.add_field(name = "12:00",value = puts[3],inline=True)
    out_weather.add_field(name = "15:00",value = puts[4],inline=True)
    out_weather.add_field(name = "18:00",value = puts[5],inline=True)
    out_weather.add_field(name = "21:00",value = puts[6],inline=True)
    out_weather.add_field(name = "最高気温",value = max_tmp[2],inline=False)
    out_weather.add_field(name = "最低気温",value = min_tmp[2],inline=False)
    out_weather.add_field(name = "湿度",value = "朝"+str(humidity[2])+"→"+"夜"+str(humidity[4]),inline=False)
    await channel.send(embed = out_weather)
    #API Key (NEWS API{https://newsapi.org/})
    n_key = ''
    indeta = requests.get("http://newsapi.org/v2/top-headlines?country=jp&apiKey="+n_key)


    w_deta = indeta.json()

    jsontxt = json.dumps(w_deta,indent=4)

    j_data = json.loads(indeta.text)

    cnt = 0
    while(cnt < 5 ):
        title = j_data["articles"][cnt]["title"]
        t_url = j_data["articles"][cnt]["url"]
        img = j_data["articles"][cnt]["urlToImage"]
        if img is None:
            print("image has not found(404)")
            img = "https://i.pinimg.com/originals/a4/2d/d8/a42dd8bab11d67086e6a82338bbfa290.jpg"
        print(title,url,img)
        cnt = cnt + 1 

        out_news = discord.Embed(title = title,url = t_url,color = discord.Colour.green())
        out_news.set_image(url = img)
        await channel.send(embed = out_news)

    await client.close()
    try:
        sys.exit(0)
    except SystemExit:
        None



client.run(TOKEN)