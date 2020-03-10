# coding: utf-8
import os
import urllib
import urllib.parse
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
                           month=int(os.environ['S_MONTH']),
                           day=int(os.environ['S_DAY']),
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
def reply_calendar(message):
    search_word = message.body['text'].split()
    if len(search_word) == 3:
        yea = int(search_word[1])
        mon = int(search_word[2])

        text = '{0}年{1}月のカレンダーを表示します'.format(yea, mon)
        message.send(text)
        # cal = calendar.TextCalendar()
        # print(cal.prmonth(yea, mon))
        calendar.setfirstweekday(calendar.SUNDAY)
        cal = '```' + calendar.month(yea, mon, w=3) + '```'
        message.send(cal)

    else:
        message.send('こんな風に指定してください↓')
        message.send('calendar! 西暦 月')
        message.send('例: calendar! 2020 3')

# 天気予報
# @respond_to('天気|weather!')
# def weather(message):
#     search_word = message.body['text'].split()
#     if len(search_word) == 2:
#         # 追加部分
#         pref = urllib.parse.quote(search_word[1])  # 都道府県
#         print("pref:", pref)
#         # message.send('地域を以下から指定してください↓')
#         # city = message  # 地域
#         # ここまで
#
#         url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city='
#         # city_id = '130010'
#         html = urllib.request.urlopen(url + pref)
#         print("html:", html)
#         jsonfile = json.loads(html.read().decode('utf-8'))
#         title = jsonfile['title']
#         telop = jsonfile['forecasts'][0]['telop']
#         telop_icon = ''
#         if telop.find('雪') > -1:
#             telop_icon = ':snowman:'
#         elif telop.find('雷') > -1:
#             telop_icon = ':thunder_cloud_and_rain:'
#         elif telop.find('晴') > -1:
#             if telop.find('曇') > -1:
#                 telop_icon = ':partly_sunny:'
#             elif telop.find('雨') > -1:
#                 telop_icon = ':partly_sunny_rain:'
#             else:
#                 telop_icon = ':sunny:'
#         elif telop.find('雨') > -1:
#             telop_icon = ':umbrella:'
#         elif telop.find('曇') > -1:
#             telop_icon = ':cloud:'
#         else:
#             telop_icon = ':fire:'
#
#         text = title + '\n' + '今日の天気は' + telop + telop_icon + 'です！'
#         message.send(text)
#     else:
#         message.send('都道府県で指定してください(北海道は道北/道東/道南/道央の中から指定)↓')
#         message.send('例: weather! 東京')


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
        url = 'https://qiita.com/api/v2/items?page=1&per_page=5&query=stocks%3A%3E3'
        title = '+title' + '%3A' + search_word[1]
        html = urllib.request.urlopen(url + title)
        jsonfile = json.loads(html.read().decode('utf-8'))

        message.send('見つかった記事を5件表示します')

        for json_ in jsonfile:
            j_title = json_['title']
            j_url = json_['url']
            message.send(j_title)
            message.send(j_url)
    else:
        message.send('こんな風に検索してください↓')
        message.send('qiita! 検索ワード')
        message.send('例: qiita! python')

# 天気予報
weather_dic = {'北海道': {'稚内': '011000', '旭川': '012010', '留萌': '012020',
               '網走': '013010', '北見': '013020', '紋別': '013030',
                       '根室': '014010', '釧路': '014020', '帯広': '014030',
                       '室蘭': '015010', '浦河': '015020', '札幌': '016010',
                       '岩見沢': '016020', '倶知安': '016030',
                       '函館': '017010', '江差': '017020'},
               '青森': {'青森': '020010', 'むつ': '020020', '八戸': '020030'},
               '岩手': {'盛岡': '030010', '宮古': '030020', '大船渡': '030030'},
               '宮城': {'仙台': '040010', '白石': '040020'},
               '秋田': {'秋田': '050010', '横手': '050020'},
               '山形': {'山形': '060010', '米沢': '060020', '酒田': '060030',
                      '新庄': '060040'},
               '福島': {'福島': '070010', '小名浜': '070020', '若松': '070030'},
               '茨城': {'水戸': '080010', '土浦': '080020'},
               '栃木': {'宇都宮': '090010', '大田原': '090020'},
               '群馬': {'前橋': '100010', 'みなかみ': '100020'},
               '埼玉': {'さいたま': '110010', '熊谷': '110020', '秩父': '110030'},
               '千葉': {'千葉': '120010', '銚子': '120020', '館山': '120030'},
               '東京': {'東京': '130010', '大島': '130020', '八丈島': '130030',
                      '父島': '130040'},
               '神奈川': {'横浜': '140010', '小田原': '140020'},
               '新潟': {'新潟': '150010', '長岡': '150020', '高田': '150030',
                      '相川': '150040'},
               '富山': {'富山': '160010', '伏木': '160020'},
               '石川': {'金沢': '170010', '輪島': '170020'},
               '福井': {'福井': '180010', '敦賀': '180020'},
               '山梨': {'甲府': '190010', '河口湖': '190020'},
               '長野': {'長野': '200010', '松本': '200020', '飯田': '200030'},
               '岐阜': {'岐阜': '210010', '高山': '210020'},
               '静岡': {'静岡': '220010', '網代': '220020', '三島': '220030',
                      '浜松': '220040'},
               '愛知': {'名古屋': '230010', '豊橋': '230020'},
               '三重': {'津': '240010', '尾鷲': '240020'},
               '滋賀': {'大津': '250010', '彦根': '250020'},
               '京都': {'京都': '260010', '舞鶴': '260020'},
               '大阪': {'大阪': '270000'},
               '兵庫': {'神戸': '280010', '豊岡': '280020'},
               '奈良': {'奈良': '290010', '風屋': '290020'},
               '和歌山': {'和歌山': '300010', '潮岬': '300020'},
               '鳥取': {'鳥取': '310010', '米子': '310020'},
               '島根': {'松江': '320010', '浜田': '320020', '西郷': '320030'},
               '岡山': {'岡山': '330010', '津山': '330020'},
               '広島': {'広島': '340010', '庄原': '340020'},
               '山口': {'下関': '350010', '山口': '350020', '柳井': '350030',
                      '萩': '350040'},
               '徳島': {'徳島': '360010', '日和佐': '360020'},
               '香川': {'高松': '370000'},
               '愛媛': {'松山': '380010', '新居浜': '380020', '宇和島': '380030'},
               '高知': {'高知': '390010', '室戸岬': '390020', '清水': '390030'},
               '福岡': {'福岡': '400010', '八幡': '400020', '飯塚': '400030',
                      '久留米': '400040'},
               '佐賀': {'佐賀': '410010', '伊万里': '410020'},
               '長崎': {'長崎': '420010', '佐世保': '420020', '厳原': '420030',
                      '福江': '420040'},
               '熊本': {'熊本': '430010', '阿蘇乙姫': '430020', '牛深': '430030',
                      '人吉': '430040'},
               '大分': {'大分': '440010', '中津': '440020', '日田': '440030',
                      '佐伯': '440040'},
               '宮崎': {'宮崎': '450010', '延岡': '450020', '都城': '450030',
                      '高千穂': '450040'},
               '鹿児島': {'鹿児島': '460010', '鹿屋': '460020', '種子島': '460030',
                       '名瀬': '460040'},
               '沖縄': {'那覇': '471010', '名護': '471020', '久米島': '471030',
                      '南大東': '472000', '宮古島': '473000', '石垣島': '474010',
                      '与那国島': '474020'}
               }

@respond_to('天気|weather!')
def weather(message):
    search_word = message.body['text'].split()
    if len(search_word) == 2:
        if weather_dic[search_word[1]]:
            text = ""
            for key in weather_dic[search_word[1]]:
                text += key + " "
            message.send('都市を選んで指定してください↓')
            message.send('例: weather! 神奈川 横浜')
            # text = weather_dic[search_word[1]].keys
            message.send(text)
            exit()
        else:
            message.send('入力が正しくありません。都道府県で指定してください')
            exit()
    elif len(search_word) == 3:
        if weather_dic[search_word[1]]:
            for key in weather_dic[search_word[1]]:
                dic_city = weather_dic[search_word[1]]
                print("dic_city:", dic_city)
                print("dic_city[key]:", dic_city[key])

                if dic_city[key]:
                    city = dic_city[key]
                else:
                    message.send('存在しない都市です。下から選んで指定してください↓')
                    message.send('例: weather! 神奈川 横浜')
                    message.send(weather_dic[search_word[1]])
                    exit()
        else:
            message.send('入力が正しくありません。都道府県で指定してください')
            exit()
        # if weather_dic[search_word[2]]:
        #     message.send('存在しない都市です。下から選んで指定してください↓')
        #     message.send('例: weather! 神奈川 横浜')
        #     message.send(weather_dic[search_word[1]])
        #     exit()
        # else:
        #     pass
        print("city:", city)
        city = urllib.parse.quote(city)  # 都市
        print("city:", city)

        url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city='
        # city_id = '130010'
        html = urllib.request.urlopen(url + city)
        print('html:', html)
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
        message.send('都道府県で指定してください↓')
        message.send('例: weather! 東京')

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
