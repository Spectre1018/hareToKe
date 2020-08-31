import sys
from bs4 import BeautifulSoup
import requests
import json
import discord
import datetime
import jpholiday


# 自分のBotのアクセストークンに置き換えてください
TOKEN = ''

CHANNNEL = "" #朝の訪れ
# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('complete set up.')
    await client.wait_until_ready()
    channel = client.get_channel(int(CHANNNEL))
    await channel.send("```おはよう！```")
    now = datetime.datetime.now()
    today = now.date()
    holy = ""
    sendy = ""
    if jpholiday.is_holiday(today) == True:
        holy = jpholiday.is_holiday_name(today)
        sendy = "```今日は{}だよ！```".format(holy)
        print(sendy)
        await channel.send(sendy)
    else:
        None

    print("ON")                
    #weather
    city = "Osaka"#居住区の名称を入力
    key = ''#OpenWeatherAPIのAPIKEYを入力 
    url = 'http://api.openweathermap.org/data/2.5/weather?units=metric&q=' + city + '&APPID=' + key


    get_deta = requests.get(url)

    w_deta = get_deta.json()
    jsontxt = json.dumps(w_deta,indent=4)

    j_data = json.loads(get_deta.text)

    puts = "as"
    pic_url = "https"
    # tenki
    icon = j_data["weather"][0]["icon"]
    if(icon == "01d" or icon == "01n"):
        puts = "快晴"
        pic_url = "https://2.bp.blogspot.com/-MiwjOj9wUCU/VyNdyBB6cLI/AAAAAAAA6Pg/PWIW9l-SF-Y87qvNT6QkdXS0lMAw4abOQCLcB/s800/window01_hare.png"
    elif(icon == "02d" or icon == "02n"):
        puts = "晴れ"
        pic_url = "https://2.bp.blogspot.com/-ltRRIC20k6E/VyNdyusNc6I/AAAAAAAA6Pk/vhRjFlTWj54h25mhVhOfEuxaWiQL6BVgQCLcB/s800/window02_aozora.png"
    elif(icon == "03d" or icon == "04d" or icon == "03n" or icon == "04n"):
        puts = "くもり"
        pic_url = "https://3.bp.blogspot.com/-g7dfhcRwb-Q/VyNd0Bg63YI/AAAAAAAA6Pw/5JzUyvksEOsdfEMILxIfl2RbivnLc9q6wCLcB/s800/window05_kumori.png"
    elif(icon == "09d" or icon == "09n"):
        puts = "小雨"
        pic_url = "https://4.bp.blogspot.com/-XB-8H9-2kPQ/VyNd1qUmQkI/AAAAAAAA6P0/FRSNfHaAWtQ39ZUHnkJUxHN1PWilx9IDwCLcB/s800/window06_ame.png"
    elif(icon == "10d" or icon == "10n"):
        puts = "雨"
        pic_url = "https://4.bp.blogspot.com/-XB-8H9-2kPQ/VyNd1qUmQkI/AAAAAAAA6P0/FRSNfHaAWtQ39ZUHnkJUxHN1PWilx9IDwCLcB/s800/window06_ame.png"
    elif(icon == "11d" or icon == "11n"):
        puts = "雷雨"
        pic_url = "https://1.bp.blogspot.com/-q1RowVJPv_E/VyNd3m3687I/AAAAAAAA6QE/_q8hiktxQj8nQbYzaRlnayDr55XDIV2zwCLcB/s800/window10_arashi.png"
    elif(icon == "13d" or icon == "13n"):
        puts = "雪"
        pic_url = "https://1.bp.blogspot.com/-mPp15Hv_kCQ/VyNd2ATyaII/AAAAAAAA6P8/vRhfkg5L7jE7QyhuuWGm-SINaFEjFWoUwCLcB/s800/window08_yuki.png"
    elif(icon == "50d" or icon == "50n"):
        puts = "霧"
        pic_url = "https://3.bp.blogspot.com/-cxYF1nh7jgQ/WOdEAeCvVEI/AAAAAAABDng/JSPTXndnhJEL5qh67Zq5N9Tz12X6svdMQCLcB/s400/yama_kiri.png"
    # sakikoukion
    max_temp = str(j_data["main"]["temp_max"])
    # saiteikion
    min_temp = str(j_data["main"]["temp_min"])
    # situdo
    hmdy = str(j_data["main"]["humidity"])


    print(puts,max_temp,min_temp,hmdy)
    out_weather = discord.Embed(title = "今日の大阪府の天気！",color = discord.Colour.from_rgb(18,207,224))
    out_weather.add_field(name = "天気", value = puts,inline=False)
    out_weather.add_field(name = "最高気温",value = max_temp,inline=False)
    out_weather.add_field(name = "最低気温",value = min_temp,inline=False)
    out_weather.add_field(name = "湿度",value = hmdy,inline=False)
    out_weather.set_thumbnail(url = pic_url)
    await channel.send(embed = out_weather)
    # await channel.send("おはようございます！\n7:30分だよ！全員起床！\n今日の大阪府の天気は・・・\n"+"天気："+ puts + "最高気温:" + max_temp + "最低気温：" + min_temp + "湿度：" + hmdy)



    indeta = requests.get("")#newsAPIのAPI_KEY


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
            img = "https://i.pinimg.com/originals/a4/2d/d8/a42dd8bab11d67086e6a82338bbfa290.jpg"#newsAPIから帰ってきたJSONにURL_Imageがない場合の画像
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



# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)