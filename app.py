from flask import Flask
from config import PORT, HOST

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'TechVJ'


if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=False)
