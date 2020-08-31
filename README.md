# ハレとケBot
## 使い方
Herokuのタイムスケジューラーを前提に書いています。
## コードの詳細
- コード中のTOKENにはDiscordのBotトークンを入力
    CHANNNELにはメッセージを吐いてほしいチャンネルIDを入力
    25行目：city = ""居住区の名称を入力
    26行目：key = ''#OpenWeatherAPIのAPIKEYを入力 
    101行目：img = ""#newsAPIから帰ってきたJSONにURL_Imageがない場合の画像
    requirements.txt、runtime.txt、ProcfileはHerokuで動作させるためのファイルです。
