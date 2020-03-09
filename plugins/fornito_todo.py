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
