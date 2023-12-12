from module.getPirateInfo import PirateDataCrawler
from flask import Flask, request, jsonify
from flask_cors import CORS
# 크롤러 모듈
pdc = PirateDataCrawler()

server = Flask(__name__)

cors = CORS(server,resources={r"/pirate":{"origins":"*"}})

# API 엔드포인트 정의
@server.route('/pirate', methods=['POST'])
def get_data():
    country_name = request.json.get('country_name')  # 요청에서 나라 이름 가져오기
    if country_name:
        result = pdc.getPirateData(country_name)  # 데이터 처리 함수 호출
        # print(result)
        return jsonify(result)
    else:
        return jsonify({'error': 'Invalid country name'})

if __name__ == '__main__':
    server.run(host='0.0.0.0',port=8080)

