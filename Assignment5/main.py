from flask import Flask,  request, escape, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('indexbill.html')


if __name__ == '__main__':
    app.run()
