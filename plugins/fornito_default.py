# coding: utf-8
from slackbot.bot import default_reply
import os
import pya3rt


@default_reply()
def default_func(message):
    """default reply"""
    apikey = os.environ['TALK_API_KEY']
    client = pya3rt.TalkClient(apikey)
    reply_message = client.talk(message.body['text'])
    message.reply(reply_message['results'][0]['reply'])
