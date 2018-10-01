from flask import Flask, render_template, request, redirect, url_for
import numpy as np

#自身をappという名前でインスタンス化する
app = Flask(__name__)

#メッセージをランダムに表示するメソッド
def picked_up():
    messages = [
        "名前を入力してください。",
        "名前はなんですか？",
        "名前を入れてね。"
    ]
    #NumPy のrandom.choiceで配列からランダムに取り出す
    return np.random.choice(messages)


##ここからWebアプリ用ルーティング
#index　にアクセスしたときの処理
@app.route('/')
def index():
    title = "ようこそ"
    message = picked_up()
    #index.htmlをレンダリングする
    return render_template('index.html',
    message=message, title=title)

# /post　にアクセスしたときの処理
@app.route('/post', methods=['GET', 'POST'])
def post():
    title = "こんにちは"
    if request.method == 'POST':
        #フォームから「名前」取得
        name = request.form['name']
        #index.htmlをレンダリング
        return render_template('index.html',
        name=name, title=title)



if __name__ == '__main__':
    app.debug = True #デバッグモード
    app.run(host='0.0.0.0') #どこからでもアクセス可能

    