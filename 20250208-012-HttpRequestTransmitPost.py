#!/usr/bin/env python3

import requests

url = "http://localhost:5000/receive"
data = "こんにちは、サーバー！"

response = requests.post(url, data=data)
print(response.text)  # サーバーからの応答を表示

