from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key'
# about.html 내에 csfr_token 에 접근하기 위한 설정 / Key to generate csfr_token

from route import *

if __name__ == '__main__':
    app.run(debug=True)