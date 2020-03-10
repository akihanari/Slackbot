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
- Slack
- Heroku

## 使い方

### ローカル環境で動かす場合（PC起動時のみ動作）
1. リポジトリをクローン
2. [こちらのURL]()にサインインして、カスタムインテグレーションを追加
3. Slack APIを取得
4. Talk APIを取得
5. PCに環境変数を設定()
```
$export SLACKBOT_API_TOKEN='SlackAPIキー'
$export TALK_API_KEY='TalkAPIキー'
```
6. ```$python run.py```

### Herokuで常時稼働させる場合
1. リポジトリをフォーク
2. [こちらのURL]()にサインインして、カスタムインテグレーションを追加
3. Slack APIを取得
4. Talk APIを取得
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

# Dependency
使用言語とバージョン、必要なライブラリとそのバージョンを書く
Pythonならrequirements.txtを用意するのも良い

# Setup
セットアップ方法を書く。用意するハードウェアとソフトウェアをセットアップするためのコマンドを記載する

# Usage
使い方。なるべく具体的に書く。サンプルも書く

# License
This software is released under the MIT License, see LICENSE.

# Authors
作者を明示する。特に、他者が作成したコードを利用する場合は、そのコードのライセンスに従った上で、リポジトリのそれぞれのコードのオリジナルの作者が誰か分かるように明示する（私はそれが良いと思い自主的にしています）。

# References
参考にした情報源（サイト・論文）などの情報、リンク

-->
