from flask import Flask, Response
from flask import request
import requests, json
import equations
app = Flask(__name__)

baseUrl = 'http://predata-challenge.herokuapp.com'
signalsUrl = baseUrl + '/signals/'
patternsUrl = baseUrl + '/patterns/'

@app.route('/')
def index():
    return "Predata"

@app.route('/signals/norm/<id>')
def normalize(id):
    #Todo: if id is outside of range, return some sort of message exception
    response = requests.get(signalsUrl + str(id))
    json_data = json.loads(response.text)
    values = [dict['value'] for dict in json_data]
    dates = [dict['date'] for dict in json_data]
    normalized_values = equations.normalize(values)
    noramilized_json = [ {"date":date, "value":value} for date, value in zip(dates, normalized_values)]
    response = Response(response = json.dumps(noramilized_json), status= 200, mimetype="application/json")
    return response

@app.route('/signals/zscore/<id>')
def zscore(id):
    window = request.args.get('window')
    return "the id is {0}, the window param is {1}".format(id, window)