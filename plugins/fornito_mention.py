# coding: utf-8
import urllib
import json
import datetime
from slackbot.bot import respond_to     # @botname: で反応するデコーダ
#
# # @respond_to('string')     bot宛のメッセージ
# #                           stringは正規表現が可能 「r'string'」
# # @listen_to('string')      チャンネル内のbot宛以外の投稿
# #                           @botname: では反応しないことに注意
# #                           他の人へのメンションでは反応する
# #                           正規表現可能
# # @default_reply()          DEFAULT_REPLY と同じ働き
# #                           正規表現を指定すると、他のデコーダにヒットせず、
# #                           正規表現にマッチするときに反応
# #                           ・・・なのだが、正規表現を指定するとエラーになる？
#
# # message.reply('string')   @発言者名: string でメッセージを送信
# # message.send('string')    string を送信
# # message.react('icon_emoji')  発言者のメッセージにリアクション(スタンプ)する
# #                               文字列中に':'はいらない
@respond_to('おはよ')
def mention_func(message):
    message.reply('おはようございます！')  # メンション


@respond_to('かわいい|ｶﾜｲｲ|kawaii')
def cute_func(message):
    message.reply('ありがとうございます:heart_eyes_cat:')     # メンション
    message.react('heart_eyes_cat')     # リアクション


@respond_to('ありがとう')
def thanks_func(message):
    message.reply('どういたしまして!')     # メンション


@respond_to('^にゃ|みゃ[ぁ|あ|-]*$')
def mention_nya(message):
    message.reply('にゃにゃん！:kissing_cat:')  # メンション
    message.react('cat')     # リアクション

# カウントダウン
@respond_to('[Pp]iscine')
def mention_42(message):
    pt = datetime.datetime(year=4242, month=4, day=2, hour=12)
    # nt = datetime.datetime.now()
    nt = datetime.datetime.today()
    rt = str(pt - nt)
    text = 'piscine開始まであと' + rt + 'です。' + ':swimmer:'
    message.reply(text)  # メンション


@respond_to(r'^ping\s+\d+\.\d+\.\d+\.\d+\s*$')
def ping_func(message):
    message.reply('それはpingのコマンドですね。実行できませんが')   # メンション


# 天気予報
@respond_to('天気|weather!')
def weather(message):
    url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city='
    city_id = '130010'
    html = urllib.request.urlopen(url + city_id)
    jsonfile = json.loads(html.read().decode('utf-8'))
    title = jsonfile['title']
    telop = jsonfile['forecasts'][0]['telop']
    telop_icon = ''
    if telop.find('雪') > -1:
        telop_icon = ':snowman:'
    elif telop.find('雷') > -1:
        telop_icon = ':thunder_cloud_and_rain:'
    elif telop.find('晴') > -1:
        if telop.find('曇') > -1:
            telop_icon = ':partly_sunny:'
        elif telop.find('雨') > -1:
            telop_icon = ':partly_sunny_rain:'
        else:
            telop_icon = ':sunny:'
    elif telop.find('雨') > -1:
        telop_icon = ':umbrella:'
    elif telop.find('曇') > -1:
        telop_icon = ':cloud:'
    else:
        telop_icon = ':fire:'

    text = title + '\n' + '今日の天気は' + telop + telop_icon + 'です！'
    message.send(text)


# 電車遅延情報
@respond_to('電車|delay!')
def train(message):
    url = 'https://tetsudo.rti-giken.jp/free/delay.json'
    html = urllib.request.urlopen(url)
    jsonfile = json.loads(html.read().decode('utf-8'))

    for json_ in jsonfile:
        name = json_['name']
        company = json_['company']
        text = company + name + 'が遅延してるみたいです...'
        message.send(text)


# ヘルプ
@respond_to('help!')
def reply_hello(message):
    attachments = [
        {
            'color': "#66CDAA",
            'fields': [
                {'title': "コマンド", 'value': "help!", 'short': True},
                {'title': "説明", 'value': "ヘルプを表示します", 'short': True},
                {'value': "weather!", 'short': True},
                {'value': "天気予報を表示します", 'short': True},
                {'value': "delay!", 'short': True},
                {'value': "電車の遅延情報を表示します", 'short': True},
            ]
        }
    ]
    message.send_webapi('コマンド一覧', json.dumps(attachments))
