from flask import Flask
app = Flask(__name__)

@app.route('/app')
def hello():
    string = 'Hello World :) + ' + $TESTE
    return string

if __name__ == '__main__':
    app.run(port=5000, debug=True)