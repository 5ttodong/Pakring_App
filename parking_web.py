from flask import Flask, render_template

parking = Flask(__name__) # 서버 하나를 만듬


@parking.route("/") # 라우팅 '/' 홈페이지를 의미.
def home():
    return render_template("parking2.html") # render_tmeplate -> html파일 만들어서 분리 가능

if __name__ == "__main__":
    parking.run(host="127.0.0.1", port=5001, debug=True)
#host="127.0.0.1", port=5001 // debug=True -> 코드를 바꿀 때마다 자동으로 재시작