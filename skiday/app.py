from flask import Flask, jsonify
import server.storage as storage

app = Flask(__name__)


@app.route('/resort/<resort>')
def resort_data(resort):
    return jsonify(storage.get_resort_data(resort))


@app.route('/')
def all_data():
    return jsonify(storage.get_all_resort_data())
