# save this as app.py
from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return name

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')