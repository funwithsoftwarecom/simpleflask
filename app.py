'''
Created on Apr 20, 2019

@author: tommoody
'''
from flask import Flask, render_template
from flask import request
from flask import jsonify
import requests
import json
import config

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


@app.route("/add", methods=['GET'])
def add_numbers():
    x = int(request.args.get('x'))
    y = int(request.args.get('y'))
    z = x+y
    response = {'answer':z}
    return jsonify(response)

@app.route("/testapi",methods=['GET'])
def get_response():
    api_link = request.args.get('apilink')
    parameters = {"lat":40.71,"lon":-74}
    print(api_link)
    req = requests.get(api_link,parameters)
    return req.content


@app.route("/tvapi",methods=['GET'])
def get_shows():
    show = request.args.get('show_name')
    x_rapidapi_key = config.rapidapi
    api_link = "https://tvjan-tvmaze-v1.p.rapidapi.com/search/shows"
    parameters = {"q":show}
    headers = {"X-RapidAPI-Key":x_rapidapi_key}
    print(api_link)
    req = requests.get(api_link,parameters,headers=headers)
    json_data = json.loads(req.text)
    
    
    return render_template("shows.html",template_data = json_data)



if __name__ == '__main__':
    app.run(debug=True)