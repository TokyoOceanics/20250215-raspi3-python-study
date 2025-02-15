#!/usr/bin/evn python3

import requests

url = "http://localhost:5000/receive"

# GETリクエストの送信
response_get = requests.get(url, params={"message": "こんにちは（GET）"})
print("GETの応答:", response_get.text)

# POSTリクエストの送信
response_post = requests.post(url, data="こんにちは（POST）")
print("POSTの応答:", response_post.text)

