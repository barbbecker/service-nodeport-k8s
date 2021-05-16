from flask import Flask
import os

app = Flask(__name__)

key = 'TESTE'
value = os.getenv(key)

@app.route('/app')
def hello():
    return('Hello Word %s' % value)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)