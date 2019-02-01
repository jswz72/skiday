from flask import Flask, jsonify
import server.storage as storage

app = Flask(__name__)


@app.route('/resort/<resort>')
def hello_world(resort):
    return jsonify(storage.get_resort_data(resort))
