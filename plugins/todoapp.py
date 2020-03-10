import os
import logging
import slack
import ssl as ssl_lib
import certifi
# from fornito_todo import Todo
from slackbot.bot import respond_to     # @botname: で反応するデコーダ

class Todo:
    """Constructs the todo message and stores the state of which tasks
     were completed."""

    TODO_BLOCK = {
       "type": "section",
       "text": {
           "type": "mrkdwn",
           "text": (
               "こんにちは！:wave:今日もお仕事頑張りましょう！:blush:\n\n"
               "*本日のタスク*"
           ),
       },
    }
    DIVIDER_BLOCK = {"type": "divider"}

    def __init__(self, channel):
        self.channel = channel
        self.username = "todo"
        self.icon_emoji = ":ghost:"
        self.timestamp = ""
        self.reaction_task_completed = False
        self.pin_task_completed = False

    def get_message_payload(self):
        return {
            "ts": self.timestamp,
            "channel": self.channel,
            "username": self.username,
            "icon_emoji": self.icon_emoji,
            "blocks": [
                self.TODO_BLOCK,
                self.DIVIDER_BLOCK,
                *self._get_reaction_block(),
                self.DIVIDER_BLOCK,
                *self._get_pin_block(),
            ],
        }

    def _get_reaction_block(self):
        task_checkmark = self._get_checkmark(self.reaction_task_completed)
        text = (
            f"{task_checkmark} *このタスクが完了したら絵文字をメッセージにつけましょう* :thinking_face:\n"
            "こちらのメッセージに絵文字をつけると、チェックマークが完了済みになります。"
            "ご自身でカスタマイズすることで、タスクごとに違う絵文字を指定することもできます。"
        )
        information = (
            ":information_source: *<https://note.mu/jinbay"
            "|Noteはこちら>*"
        )
        return self._get_task_block(text, information)

    def _get_pin_block(self):
        task_checkmark = self._get_checkmark(self.pin_task_completed)
        text = (
            f"{task_checkmark} *このタスクが完了したらメッセージにピンをしましょう* :round_pushpin:\n"
            "こちらのメッセージにピンをすると、チェックマークが完了済みになります。"
            "重要なメッセージなどをピン留めして、あとで効率よく確認することができます。"
        )
        information = (
            ":information_source: *<https://twitter.com/jinbay_tech"
            "|Twitterはこちら>*"
        )
        return self._get_task_block(text, information)

    @staticmethod
    def _get_checkmark(task_completed: bool) -> str:
        if task_completed:
            return ":white_check_mark:"
        return ":white_large_square:"

    @staticmethod
    def _get_task_block(text, information):
        return [
            {"type": "section", "text": {"type": "mrkdwn", "text": text}},
            {"type": "context", "elements":
             [{"type": "mrkdwn", "text": information}]},
        ]

# アプリをシンプルにするために、データをメモリ上に保存
# todo_sent = {"channel": {"user_id": todo}}
todo_sent = {}
# if __name__ == "__main__":
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())
# ここらへん怪しい
ssl_context = ssl_lib.create_default_context(cafile=certifi.where())
slack_token = os.environ['SLACKBOT_API_TOKEN']
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
@respond_to('todo!')
@slack.RTMClient.run_on(event="message")
def message(**payload):
    """
    Slackから "todo!" が含まれるメッセージが送られたときにTodoメッセージを投稿
    """
    data = payload["data"]
    web_client = payload["web_client"]
    channel_id = data.get("channel")
    user_id = data.get("user")
    # text = data.get("text")

    # if text and text.lower() == "todo!":
    return start_todo(web_client, user_id, channel_id)
