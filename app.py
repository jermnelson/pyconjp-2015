__author__ = "Jeremy Nelson"
__version__ = '0.1.0'

from flask import Flask, abort, render_template

app = Flask(__name__)

@app.route("/slides/<name>")
def suradio(name):
    return render_template('slides/{}.html'.format(name))

@app.route("/")
def homu():
    return render_template('index.html')

def mein():
    app.run(host='0.0.0.0', port=21511, debug=True)

if __name__ == '__main__':
    mein()
