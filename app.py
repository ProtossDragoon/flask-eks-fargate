"""플라스크 웹 애플리케이션
"""
from flask import Flask
from flask import jsonify

import change

app = Flask(__name__)

@app.route('/')
def hello():
    """안내 문구를 보여줍니다.
    """
    print('hello() 함수가 실행됨')
    return 'Hello World! `/change/{금액}` 으로 접속하세요.'

@app.route('/change/<money>')
def change_route(money):
    """거스름돈을 계산합니다.
    """
    print(f'Make Change for {money}')
    result = change.Algorithm(int(money), coin_types={10, 50, 100, 500}).calculate(ret_dict=True)
    return jsonify(result)
