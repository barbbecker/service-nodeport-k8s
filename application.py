from flask import Flask
app = Flask(__name__)

@app.route('/app')
def hello():
    return 'Hello Word :)'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)