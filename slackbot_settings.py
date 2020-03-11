# coding: utf-8
import os
# import pya3rt
# from slackbot.bot import default_reply  # 該当する応答がない場合に反応するデコーダ

# SlackAPIトークンを指定
API_TOKEN = os.environ['SLACKBOT_API_TOKEN']

# このbot宛のメッセージで、どのパターンにも当てはまらない場合の応答（Talk API）
# @default_reply()
# def default_func(message):
#     apikey = os.environ['TALK_API_KEY']
#     client = pya3rt.TalkClient(apikey)
#     reply_message = client.talk(message.body['text'])
#     message.reply(reply_message['results'][0]['reply'])


# プラグインスクリプトを置いてあるサブディレクトリ名のリスト
PLUGINS = [
    'plugins',
]
