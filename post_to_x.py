import os
import requests
from requests_oauthlib import OAuth1

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
        tweet_content = value
        url = "https://api.twitter.com/2/tweets"
        payload = {"text": tweet_content}

        response = requests.post(url, auth=auth, json=payload)

        if response.status_code == 201:
            print(f"Successfully posted to X: {tweet_content}")
        else:
            print(f"Failed to post to X: {response.status_code}")
            print(response.json())

