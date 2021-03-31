import json
import os
import uuid
import pandas as pd
from flask import Flask, jsonify, make_response, request
from flask_cors import CORS
from pathlib import Path

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = "xud40"


@app.route('/api/v1/test', methods=['GET'])
def testApi():
    return "Azy Agric. API Reachable"


# get json data
@app.route('/api/v1/getJsonData', methods=['GET'])
def getJsonData():
    file_path = Path(__file__).with_name('interview.json')
    with file_path.open('r') as json:
        data = json.read()

    print(data)

    if data is None:
        return jsonify({
            'code': 400,
            'message': 'The request could not be handled at this time'
        })
    else:
        return jsonify({
            'code': 200,
            'data': data
        })


if __name__ == "__main__":
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    app.run(HOST, 5000, debug=True)
