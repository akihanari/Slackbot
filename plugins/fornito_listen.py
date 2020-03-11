# coding: utf-8
from slackbot.bot import listen_to      # チャネル内発言で反応
#
# # @listen_to('string')      チャンネル内のbot宛以外の投稿
# #                           @botname: では反応しないことに注意
# #                           他の人へのメンションでは反応する
# #                           正規表現可能


@listen_to('fornito|ふぉにと')
def listen_func(message):
    message.send('へっくしゅん！')
    message.reply('お呼びですか？')
    message.react('heart_eyes_cat')
