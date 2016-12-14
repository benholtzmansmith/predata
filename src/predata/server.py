import json
import requests
from datetime import datetime
from flask import Flask, Response
from flask import request

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
    response = requests.get(signalsUrl + str(id))
    window = float(request.args.get('window'))
    json_data = json.loads(response.text)
    values = [x['value'] for x in json_data]
    formated_dates = [datetime.strptime(x['date'],'%Y-%m-%d') for x in json_data]
    formatted_json = [ {"date":date, "value":value} for date, value in zip(formated_dates, values)]
    z_scores = [
        equations.compute_z_score(
                equations.filter_by_date(formatted_json, date_dict, window),
                date_dict['value']
            ) for date_dict in formatted_json
        ]
    transformed_response = [ {"date":date_value_dict['date'], "value":z_score} for (date_value_dict, z_score) in zip(json_data, z_scores)]
    response = Response(response = json.dumps(transformed_response), status= 200, mimetype="application/json")
    return response

@app.route('/signals/combine/')
def linear_combination():
    signal_wieght = request.args
    values = signal_wieght.getlist('signal')
    split_values = [x.split(',') for x in values]
    linear_combinations = [
        equations.compute_linear_combination(
            [dict['value'] for dict in json.loads(requests.get(signalsUrl + str(signalId)).text)],
            float(weight)
        ) for (signalId, weight) in split_values
    ]
    response = Response(response = json.dumps(linear_combinations), status= 200, mimetype="application/json")
    return response
