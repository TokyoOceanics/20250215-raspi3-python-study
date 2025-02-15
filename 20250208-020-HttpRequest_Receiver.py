#!/usr/bin/python3

#pip install flask
# 2025/02/09
#chat GPT


from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/test", methods=["GET", "POST"])
def handle_request():
    if request.method == "GET":
        data = request.args.to_dict()  # クエリパラメータ取得
        return jsonify({"received": "GET", "data": data})
    
    elif request.method == "POST":
        data = request.json  # JSONデータ取得
        return jsonify({"received": "POST", "data": data})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
