# coding: utf-8
import os
import json
import webapp2
# botアカウントのトークンを指定

class EchoHandler(webapp2.RequestHandler):
    VERIFICATION_TOKEN = os.environ['SLACKBOT_VERIFICATION_TOKEN']
    # API_TOKEN = os.environ['SLACKBOT_API_TOKEN']

    def post(self):
        body = json.loads(self.request.body)
        if body['token'] != self.VERIFICATION_TOKEN:
            self.response.headers['Content-Type'] = 'text/plain'
            self.status = 403
            self.response.write('403 Forbidden')
            return
        if body['type'] == 'url_verification':
            self.verify_url(body)

    def verify_url(self, params):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(params['challenge'])

app = webapp2.WSGIApplication([
    ('/echo-bot-hook', EchoHandler)
], debug=True)


# API_TOKEN = os.environ['SLACKBOT_API_TOKEN']

# このbot宛のメッセージで、どの応答にも当てはまらない場合の応答文字列
DEFAULT_REPLY = "すみません、よくわかりません。"

# プラグインスクリプトを置いてあるサブディレクトリ名のリスト
PLUGINS = [
    'plugins',
]
