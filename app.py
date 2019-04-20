'''
Created on Apr 20, 2019

@author: tommoody
'''
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


if __name__ == '__main__':
    app.run(debug=True)