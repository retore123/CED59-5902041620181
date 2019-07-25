from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def index():
    return"hello WORLD"
if __name__ == '_main__':
    app.run()