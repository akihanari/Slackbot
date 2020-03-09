import os
import logging
import slack
import ssl as ssl_lib
import certifi
from fornito_todo import Todo

# アプリをシンプルにするために、データをメモリ上に保存
# todo_sent = {"channel": {"user_id": todo}}
todo_sent = {}

# if __name__ == "__main__":
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())
ssl_context = ssl_lib.create_default_context(cafile=certifi.where())
slack_token = os.environ["SLACK_BOT_TOKEN"]
rtm_client = slack.RTMClient(token=slack_token, ssl=ssl_context)
rtm_client.start()

def start_todo(web_client: slack.WebClient, user_id: str, channel: str):
    # 新しいTodoインスタンスを作成
    todo = Todo(channel)

    # Todoメッセージを取得
    message = todo.get_message_payload()

    # TodoメッセージをSlackに投稿
    response = web_client.chat_postMessage(**message)

    # 先ほど投稿したメッセージのタイムスタンプを保存
    # あとでユーザーがTodoタスクを完了したときに、このタイムスタンプを利用してメッセージを更新
    todo.timestamp = response["ts"]

    # todo_sentにメッセージを保存
    if channel not in todo_sent:
        todo_sent[channel] = {}
    todo_sent[channel][user_id] = todo


# ============= Reaction Added Events ============= #
# ユーザーが絵文字でメッセージにリアクションをしたときに呼ばれるメソッド
# イベントタイプは 'reaction_added'
@slack.RTMClient.run_on(event="reaction_added")
def update_emoji(**payload):
    """
    Slackから "reaction_added" のイベントを受け取ったあとに、Todoメッセージを更新
    対象のメッセージはタイムスタンプを元に判定
    """
    data = payload["data"]
    web_client = payload["web_client"]
    channel_id = data["item"]["channel"]
    user_id = data["user"]

    if channel_id not in todo_sent:
        return

    # Slackに投稿したTodoメッセージを取得
    todo = todo_sent[channel_id][user_id]

    # タスクを完了済みに更新
    todo.reaction_task_completed = True

    # 新しいメッセージを取得
    message = todo.get_message_payload()

    # 更新されたメッセージをSlackに投稿
    updated_message = web_client.chat_update(**message)

    # タイプスタンプを更新
    todo.timestamp = updated_message["ts"]


# =============== Pin Added Events ================ #
# ユーザーがメッセージをピン留めしたときに呼ばれるメソッド
# イベントタイプは 'pin_added'
@slack.RTMClient.run_on(event="pin_added")
def update_pin(**payload):
    """
    Slackから "pin_added" のイベントを受け取ったあとに、Todoメッセージを更新
    対象のメッセージはタイムスタンプを元に判定
    """
    data = payload["data"]
    web_client = payload["web_client"]
    channel_id = data["channel_id"]
    user_id = data["user"]

    # Slackに投稿したTodoメッセージを取得
    todo = todo_sent[channel_id][user_id]

    # タスクを完了済みに更新
    todo.pin_task_completed = True

    # 新しいメッセージを取得
    message = todo.get_message_payload()

    # 更新されたメッセージをSlackに投稿
    updated_message = web_client.chat_update(**message)

    # タイプスタンプを更新
    todo.timestamp = updated_message["ts"]


# ============== Message Events ============= #
# ユーザーがDMを送ったときに呼ばれるイベント
# イベントタイプは 'message'
@slack.RTMClient.run_on(event="message")
def message(**payload):
    """
    Slackから "todo!" が含まれるメッセージが送られたときにTodoメッセージを投稿
    """
    data = payload["data"]
    web_client = payload["web_client"]
    channel_id = data.get("channel")
    user_id = data.get("user")
    text = data.get("text")

    if text and text.lower() == "todo!":
        return start_todo(web_client, user_id, channel_id)
