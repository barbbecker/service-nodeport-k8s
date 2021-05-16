from flask import Flask
import os

app = Flask(__name__)

key = 'TESTE_BARBARA'
value = os.getenv(key)

@app.route('/app')
def hello():
    return('Hello Word %s' % value)

if __name__ == '__main__':
    app.run(port=5000, debug=True)