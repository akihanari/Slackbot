# coding: utf-8
import os
import urllib
import json
import datetime
import calendar
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
def mention_morning(message):
    message.reply('おはようございます！')  # メンション


@respond_to('こんにちは')
def mention_afternoon(message):
    message.reply('こんにちは！')  # メンション


@respond_to('こんばんは')
def mention_evening(message):
    message.reply('こんばんは！')  # メンション


@respond_to('おやすみ')
def mention_goodnigt(message):
    message.reply('おやすみなさいませ！')  # メンション


@respond_to('ただいま')
def mention_home(message):
    message.reply('おかえりなさいませ！')  # メンション


@respond_to('いってきます')
def mention_leave(message):
    message.reply('いってらっしゃいませ！')  # メンション


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
@respond_to(os.environ['S_COM'])
def mention_42(message):
    pt = datetime.datetime(year=int(os.environ['S_YEAR']),
         month=int(os.environ['S_MONTH']), day=int(os.environ['S_DAY']),
           hour=int(os.environ['S_HOUR']))
    # nt = datetime.datetime.now()ß
    nt = datetime.datetime.today()
    rt = str(pt - nt)
    text = os.environ['S_WORD'] + '開始まであと' + rt + 'です' + ':swimmer:'
    message.reply(text)  # メンション


@respond_to(r'^ping\s+\d+\.\d+\.\d+\.\d+\s*$')
def ping_func(message):
    message.reply('それはpingのコマンドですね。実行できませんが')   # メンション


# カレンダー
@respond_to('calendar!')
def reply_qiita(message):
    search_word = message.body['text'].split()
    if len(search_word) == 3:
        yea = search_word[1]
        mon = search_word[2]

        message.send(yea, '年', mon, '月のカレンダーを表示します')
        cal = calendar.TextCalendar()
        cal.prmonth(yea, mon)

    else:
        message.send('こんな風に指定してください↓')
        message.send('calendar! 西暦 月')
        message.send('例: calendar! 2020 3')

# 天気予報
@respond_to('天気|weather!')
def weather(message):
    search_word = message.body['text'].split()
    if len(search_word) == 2:
        # 追加部分
        pref = search_word[1]  # 都道府県
        # message.send('地域を以下から指定してください↓')
        # city = message  # 地域
        # ここまで

        url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city='
        # city_id = '130010'
        html = urllib.request.urlopen(url + pref)
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
    else:
        message.send('都道府県で指定してください(北海道は道北/道東/道南/道央の中から指定)↓')
        message.send('例: weather! 東京')


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


# Qiita
@respond_to('qiita!')
def reply_qiita(message):
    search_word = message.body['text'].split()
    if len(search_word) == 2:
        url = 'https://qiita.com/api/v2/items?page=1&per_page=3&query=stocks%3A%3E3'
        title = '+title=' + '%3A' + search_word[1]
        html = urllib.request.urlopen(url + title)
        jsonfile = json.loads(html.read().decode('utf-8'))

        message.send('見つかった記事を3件表示します')

        for json_ in jsonfile:
            j_title = json_['title']
            j_url = json_['url']
            message.send(j_title)
            message.send(j_url)
    else:
        message.send('こんな風に検索してください↓')
        message.send('qiita! 検索ワード')
        message.send('例: qiita! python')


# ヘルプ
@respond_to('help!')
def reply_hello(message):
    attachments = [
        {
            'color': "#66CDAA",
            'fields': [
                {'title': "コマンド", 'value': "help!", 'short': True},
                {'title': "説明", 'value': "ヘルプを表示します", 'short': True},
                {'value': "todo!", 'short': True},
                {'value': "TODO機能を実行します", 'short': True},
                {'value': "qiita! 検索ワード", 'short': True},
                {'value': "Qiitaの記事を検索します", 'short': True},
                {'value': "weather!", 'short': True},
                {'value': "天気予報を表示します", 'short': True},
                {'value': "delay!", 'short': True},
                {'value': "電車の遅延情報を表示します", 'short': True},
                {'value': "calendar! 西暦 月", 'short': True},
                {'value': "カレンダーを表示します", 'short': True},
            ]
        }
    ]
    message.send_webapi('コマンド一覧', json.dumps(attachments))
