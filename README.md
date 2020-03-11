<!--

# Slackbot(for-ni-to)

概要概要概要概要概要概要概要概要概要概要概要概要概要概要概要概要

## 簡単な説明

簡単な説明簡単な説明簡単な説明簡単な説明簡単な説明簡単な説明簡単な説明
簡単な説明簡単な説明簡単な説明簡単な説明簡単な説明簡単な説明簡単な説明
簡単な説明簡単な説明簡単な説明簡単な説明簡単な説明簡単な説明簡単な説明
簡単な説明簡単な説明簡単な説明簡単な説明簡単な説明簡単な説明簡単な説明

***デモ***

![デモ](https://image-url.gif)

## 機能

| コマンド | 説明 | 例 |
| :-: | :-: | :-: |
| help! | ヘルプを表示します | help! |
| todo! | TODO機能を実行します | todo! |
| qiita! 検索ワード | Qiitaの記事を検索(5件のみ表示)します | qiita! Python |
| weather! 都道府県 都市 | 天気予報を表示します | weather! 神奈川 横浜 |
| delay! 路線 | 電車の遅延情報を表示します | delay! 山手線 |
| calendar! 年 月 | カレンダーを表示します | calendar! 2020 3 |


## 必要要件

- python-3.7.0
- Slackのワークスペース
- Heroku

## 使い方

### ローカル環境で動かす場合（PC起動時のみ動作）
1. リポジトリをクローンする。
2. [こちらのURL](https://my.slack.com/services/new/bot)にサインインして、カスタムインテグレーションを追加する。
3. Slack APIを取得する。
4. Talk APIを取得する。
5. PCに環境変数を設定する(下記参照)
```
$export SLACKBOT_API_TOKEN='SlackAPIキー'
$export TALK_API_KEY='TalkAPIキー'
```
6. ```$python run.py```

### Herokuで常時稼働させる場合
1. リポジトリをフォークする。
2. [こちらのURL](https://my.slack.com/services/new/bot)にサインインして、カスタムインテグレーションを追加する。
3. Slack API Tokenを取得
4. Talk API キーを取得
5. Herokuでアプリを作成
6. Herokuに環境変数を設定
| key | value |
| :-: | :-: |
| SLACKBOT_API_TOKEN | SlackAPIキー |
| TALK_API_KEY | TalkAPIキー |
7. Deploy

## インストール

```
$ git clone https://github.com/akihanari/Slackbot
$ cd Slackbot
```

## テスト

1. 使い方
2. 使い方
3. 使い方

## デプロイ

1. デプロイ
2. デプロイ
3. デプロイ

## その他

その他その他その他その他
その他その他その他その他
その他その他その他その他
その他その他その他その他

## 作者

[@TanakanoAnchan](https://twitter.com/TanakanoAnchan)
mail to: xxxx@mail.com

## ライセンス

[MIT](http://TomoakiTANAKA.mit-license.org)</blockquote>

-----------

最初にアイキャッチ画像などを表示

# リポジトリ名
このソフトはどんなもので、何ができるのかを書く
合わせて、簡単なデモ（使用例）などスクリーンショットやGIFアニメで表示
Slackbotです。主に以下の機能があります。
+ Qiita検索
+ 天気予報
+ 電車遅延情報
+ カレンダー表示
+ 雑談


# Dependency
使用言語とバージョン、必要なライブラリとそのバージョンを書く
Pythonならrequirements.txtを用意するのも良い
Python
+ Python-3.7.0
ライブラリ
 + certifi==2019.11.28
 + chardet==3.0.4
 + idna==2.9
 + pya3rt==1.1
 + requests==2.12.4
 + six==1.14.0
 + slackbot==0.5.6 *
 + slackclient==2.5.0
 + slacker==0.14.0 *
 + urllib3==1.25.8
 + websocket-client==0.44.0

# 使用API
+ SlackAPI
→Setup参照
+ [Livedoor お天気Webサービス](http://weather.livedoor.com/weather_hacks/webservice)
+ [鉄道遅延情報のjson](https://rti-giken.jp/fhc/api/train_tetsudo/)
+ [recruit-tech TalkAPI](https://a3rt.recruit-tech.co.jp/product/talkAPI/)
→メールアドレスを登録することでAPIキーを取得できる

# Setup
セットアップ方法を書く。用意するハードウェアとソフトウェアをセットアップするためのコマンドを記載する


# Usage
使い方。なるべく具体的に書く。サンプルも書く

# License
This software is released under the MIT License, see LICENSE.

# Authors
作者を明示する。特に、他者が作成したコードを利用する場合は、そのコードのライセンスに従った上で、リポジトリのそれぞれのコードのオリジナルの作者が誰か分かるように明示する（私はそれが良いと思い自主的にしています）。
akihanari

# References
参考にした情報源（サイト・論文）などの情報、リンク

Slackbotの作成
+ [ビットログ](https://blog.bitmeister.jp/?p=3911)

APIについて
+ [Slackbot備忘録(1)](https://qiita.com/usomaru/items/529b6f40902ee1eda125)
+ [リクルートのTalk APIを用いてslack bot(python製)に会話機能を追加する](https://qiita.com/takahirono7/items/197375db24a03cbcd591)

Herokuにデプロイ
+ [pythonで作ったSlackBotを常駐化するまでの備忘録](https://qiita.com/usomaru/items/6eed064690cdb7988e54)

# URL
[GitHub](https://github.com/akihanari/Slackbot)
-->
