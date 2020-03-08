# coding: utf-8
import os

# botアカウントのトークンを指定

API_TOKEN = os.environ['SLACKBOT_API_TOKEN']

# このbot宛のメッセージで、どの応答にも当てはまらない場合の応答文字列
DEFAULT_REPLY = "すみません、よくわかりません。"

# プラグインスクリプトを置いてあるサブディレクトリ名のリスト
PLUGINS = [
    'plugins',
]
