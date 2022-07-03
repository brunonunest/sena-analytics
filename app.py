# save this as app.py, for docker use only
from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def test():
    pass
    return None

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')