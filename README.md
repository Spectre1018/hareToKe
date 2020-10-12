# ハレとケBot
## 使い方
Herokuのタイムスケジューラーを前提に書いています。
## コードの詳細
- コード中のTOKENにはDiscordのBotトークンを入力
    CHANNNELにはメッセージを吐いてほしいチャンネルIDを入力
    36行目：city = ""居住区の名称を入力
    37行目：key = ''#OpenWeatherAPIのAPIKEYを入力 
    98行目：indeta = requests.get("")#newsAPIのAPI_Keyを入力
    113行目：img = ""#newsAPIから帰ってきたJSONにURL_Imageがない場合の画像（オンラインURLをセット）
    requirements.txt、runtime.txt、ProcfileはHerokuで動作させるためのファイルです。
    そのため、このままダンロードして上の４つをセットしたらそのまま使えます。
