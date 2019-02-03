from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
import server.storage as storage

app = Flask(__name__)
CORS(app)


@app.route('/resort/<resort>')
def hello_world(resort):
    return jsonify(storage.get_resort_data(resort))
