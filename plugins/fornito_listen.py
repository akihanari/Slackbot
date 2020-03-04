# coding: utf-8
from slackbot.bot import listen_to      # チャネル内発言で反応するデコーダ
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


@listen_to('fornito|ふぉにと')
def listen_func(message):
    message.send('へっくしゅん！')      # ただの投稿
    message.reply('お呼びですか？')                           # メンション
    message.react('heart_eyes_cat')     # リアクション
