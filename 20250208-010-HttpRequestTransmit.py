#!/usr/bin/env python3

import requests

class HttpClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint, params=None):
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url, params=params)
        return response.json()

    def post(self, endpoint, data=None):
        url = f"{self.base_url}/{endpoint}"
        response = requests.post(url, json=data)
        return response.json()

# 使用例
client = HttpClient("http://localhost:5000")
print(client.get("test", {"key": "value"}))  # GETリクエスト
print(client.post("test", {"message": "Hello"}))  # POSTリクエスト
