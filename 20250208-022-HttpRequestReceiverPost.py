#!/usr/bin/env python3

from flask import Flask, request

app = Flask(__name__)

@app.route("/receive", methods=["POST"])
def receive_data():
    data = request.get_data(as_text=True)  # 受信したデータを文字列として取得
    print(f"受信データ: {data}")  # コンソールに表示
    return "データを受信しました", 200  # クライアントに応答

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
