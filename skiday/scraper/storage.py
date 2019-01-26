import sqlite3
import datetime
from definitions import DB_PATH, METRICS

conn = sqlite3.connect(DB_PATH, isolation_level=None)
db = conn.cursor()

def get_resort_id(resort):
    db.execute('SELECT id from resorts where name=?', (resort,))
    return int(db.fetchone()[0])

def write_conditions(rid, conditions):
    db.execute('INSERT INTO conditions VALUES (?, ?, ?)', (rid, conditions, str(datetime.datetime.now())))

def write_metrics(rid, data):
    for metric, value in data.items():
        db.execute('SELECT id FROM metric_types WHERE type=?', (metric,))
        result = db.fetchone()
        if result:
            print(value)
            # TODO fix value data format
            db.execute('INSERT INTO metrics VALUES (?,?,?,?)', (rid, result[0],str(datetime.datetime.now()), value.join('-'))


def write_resort_data(resort, data):
    rid = get_resort_id(resort)
    write_conditions(rid, data['conditions'])
    write_metrics(rid, data)

def get_url(resort):
    rid = get_resort_id(resort)
    db.execute('SELECT url from webpages where resort=?', (rid,))
    return db.fetchone()[0]

