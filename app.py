import requests
from flask import Flask, render_template

app = Flask(__name__)

# 본인 API 인증키
API_KEY = "1a10badc8e7f0623a5db101c1f12e6eb6353993911572f56fd24fd6a0a21febd"

@app.route("/")
def weather():
    url = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst"
    params = {
        "serviceKey": API_KEY,
        "numOfRows": 10,
        "pageNo": 1,
        "dataType": "JSON",
        "base_date": "20260510",  # 오늘 날짜
        "base_time": "1100",      # 발표 시간
        "nx": 55,                 # 서울 격자 X
        "ny": 127                 # 서울 격자 Y
    }

    response = requests.get(url, params=params)
    data = response.json()

    items = data['response']['body']['items']['item']
    return render_template("index.html", items=items)

if __name__ == "__main__":
    app.run(debug=True)
