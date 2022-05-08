from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key'
# about.html 내에 csfr_token 에 접근하기 위한 설정 / Key to generate csfr_token

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
# .db 파일을 생성하기 위한 라인
"""
# 문제 발견
data.db 를 제대로 생성하기 위해선 app>db 뿐만 아니라 models>Task 를 import 해야함

: python3 에디터 접속 -> from app import db -> from models import Task
-> db.create_all() -> 폴더 내에 data.db 파일 생성

혹은

: python3 에디터 접속 -> from models import db 도 가능

* 즉, db 는 파일을 생성하기 위한 용도, Task 는 파일 안에 정보를 위한 용도임을 확인할 수 있다.
"""

app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

"""
sqlite 가 아닌 mysql 을 통해 접속을 할 경우 설정

# LOCAL

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:비밀번호@localhost/data'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '비밀번호'
app.config['MYSQL_DB'] = 'data' 
"""

db = SQLAlchemy(app)

from route import *

if __name__ == '__main__':
    app.run(debug=True)