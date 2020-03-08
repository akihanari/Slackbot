# coding: utf-8
from slackbot.bot import default_reply  # 該当する応答がない場合に反応するデコーダ
import pya3rt

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
# count = 0
#
#
# @default_reply()
# def default_func(message):
#     global count        # 外で定義した変数の値を変えられるようにする
#     count += 1
#     message.reply('%d 回目のデフォルトの返事です' % count)  # メンション


@default_reply()
def default_func(message):
    apikey = os.environ['TALK_API_KEY']
    client = pya3rt.TalkClient(apikey)
    reply_message = client.talk(message.body['text'])
    # 以下の形式でjsonが返ってくるので、replyの部分をとりだす
    # {'status': 0, 'message': 'ok', 'results': [{'perplexity': 1.2802554542585969, 'reply': '私にはよくわからないです'}]}
    message.reply(reply_message['results'][0]['reply'])
