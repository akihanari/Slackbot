# coding: utf-8
from slackbot.bot import listen_to


@listen_to('fornito|ふぉにと|for-ni-to')
def listen_func(message):
    """channel response"""
    message.send('へっくしゅん！')
    message.reply('お呼びですか？')
    message.react('heart_eyes_cat')
