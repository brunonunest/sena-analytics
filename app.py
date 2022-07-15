#code for docker build use only, creating an example of our app on docker
from flask import Flask

app = Flask(__name__)

@app.route('/')
def test():
    pass
    return None

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')