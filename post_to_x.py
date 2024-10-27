import os
import requests
from requests_oauthlib import OAuth1
import re

# OAuth 1.0a認証の設定
auth = OAuth1(
    os.getenv("API_KEY"),
    os.getenv("API_SECRET_KEY"),
    os.getenv("ACCESS_TOKEN"),
    os.getenv("ACCESS_TOKEN_SECRET")
)

# 各投稿内容を環境変数から取得してツイート
for key, value in os.environ.items():
    if key.startswith("TWEET_CONTENT_"):
        # 投稿内容からタイトルとURLを取得
        tweet_content = value
        match = re.match(r'^(.*?)という記事を作成しました！\n(https?://\S+)$', tweet_content, re.DOTALL)
        if match:
            title = match.group(1)
            url = match.group(2)

            # タグ情報を取得
            topics = os.getenv(f"TOPICS_{key.split('_')[-1]}")
            if topics:
                tags = ' '.join([f"#{topic.strip()}" for topic in topics.split(",")])
            else:
                tags = ""

            # タイトルにリンクを埋め込んで投稿内容をフォーマット
            tweet_text = f"{title} [リンクはこちら]({url})\n\n{tags}"

            # APIエンドポイント
            api_url = "https://api.twitter.com/2/tweets"
            payload = {"text": tweet_text}

            # POSTリクエストを送信
            response = requests.post(api_url, auth=auth, json=payload)

            if response.status_code == 201:
                print(f"Successfully posted to X: {tweet_text}")
            else:
                print(f"Failed to post to X: {response.status_code}")
                print(response.json())

