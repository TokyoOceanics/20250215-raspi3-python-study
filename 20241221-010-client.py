#!/usr/bin/env python3

#chat gpt https://chatgpt.com/c/675c2fa2-17c8-800f-8ccd-a25f90e3b856


import requests

# サーバーのURL
SERVER_URL = "http://127.0.0.1:5000/data"

# GETリクエストの送信
def send_get_request():
    try:
        response = requests.get(SERVER_URL)
        if response.status_code == 200:
            print("GETリクエスト成功:")
            print(response.json())  # サーバーからのレスポンスを表示
        else:
            print(f"GETリクエスト失敗: {response.status_code}")
    except Exception as e:
        print(f"GETリクエスト中にエラーが発生しました: {e}")

# POSTリクエストの送信
def send_post_request():
    try:
        data = {
            "name": "Client",
            "message": "Hello, Server!"
        }
        response = requests.post(SERVER_URL, json=data)
        if response.status_code == 200:
            print("POSTリクエスト成功:")
            print(response.json())  # サーバーからのレスポンスを表示
        else:
            print(f"POSTリクエスト失敗: {response.status_code}")
    except Exception as e:
        print(f"POSTリクエスト中にエラーが発生しました: {e}")

if __name__ == "__main__":
    print("GETリクエストを送信中...")
    send_get_request()

    print("\nPOSTリクエストを送信中...")
    send_post_request()

