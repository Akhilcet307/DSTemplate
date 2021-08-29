from flask import Flask, escape, request, jsonify, Response
from {{cookiecutter.model_slug}} import {{cookiecutter.model_class}}

import json

app = Flask(__name__)

@app.route('/api/model/{{cookiecutter.model_slug}}', methods=['POST'])
def run_model():
    
    result = {"result":""}
    response_status = 200
    try:
        
        # Dynamically load model based on URL and Query String parameters
        model = {{cookiecutter.model_class}}()
        
        #Invoke Model and capture result
        result = model.predict(data = request.get_json())

    except Exception as ex:
        result = {"error":"Unexpected exception with a message of: {0}".format(ex)}
        response_status = 500

    return Response("{0}".format(json.dumps(result)), mimetype="application/json", status=response_status)