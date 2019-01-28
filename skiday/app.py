from flask import Flask
import server.storage as storage

app = Flask(__name__)


@app.route('/resort/<resort>')
def hello_world(resort):
    return storage.get_resort_data(resort)
