import os
import requests
from requests_oauthlib import OAuth1

# OAuth 1.0a 認証の設定
auth = OAuth1(
    os.getenv("API_KEY"),
    os.getenv("API_SECRET_KEY"),
    os.getenv("ACCESS_TOKEN"),
    os.getenv("ACCESS_TOKEN_SECRET")
)

# 各投稿内容を環境変数から取得してツイート
for key, value in os.environ.items():
    if key.startswith("TWEET_CONTENT_"):
        # 投稿内容からタイトルとURL、トピックタグを取得
        page_title = key.split("TWEET_CONTENT_")[-1]
        tweet_content = value
        url = os.getenv(f"URL_{page_title}")
        topics = os.getenv(f"TOPICS_{page_title}")

        # トピックをタグ形式に変換
        tags = " ".join([f"#{topic.strip()}" for topic in topics.split(",")]) if topics else ""

        # タイトルにリンクを埋め込んだ投稿内容をフォーマット
        tweet_text = f"{tweet_content}\n\n{url}\n\n{tags}"

        # API エンドポイント
        api_url = "https://api.twitter.com/2/tweets"
        payload = {"text": tweet_text}

        # POSTリクエストを送信
        response = requests.post(api_url, auth=auth, json=payload)

        if response.status_code == 201:
            print(f"Successfully posted to X: {tweet_text}")
        else:
            print(f"Failed to post to X: {response.status_code}")
            print(response.json())

