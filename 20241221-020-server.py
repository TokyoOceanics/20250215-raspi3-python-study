#!/usr/bin/env python3

from flask import Flask, request, jsonify

app = Flask(__name__)

# GETリクエストの処理
@app.route('/data', methods=['GET'])
def get_data():

    received_data=request.post_json()
    if not received_data:
        print(received_data)
    # ダミーデータを返す
    data = {
        "message": "Hello from server!",
        "value": 42
    }
    return jsonify(data)

# POSTリクエストの処理
@app.route('/data', methods=['POST'])
def post_data():
    # クライアントから送信されたJSONデータを取得
    received_data = request.get_json()
    if not received_data:
        print(received_data )
        return jsonify({"error": "No JSON data received"}), 400

    # データを加工してレスポンスとして返す
    response_data = {
        "message": "Data received successfully",
        "received": received_data
    }
    return jsonify(response_data), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

