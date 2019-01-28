import sqlite3
import datetime
from definitions import DB_PATH, METRICS

conn = sqlite3.connect(DB_PATH, isolation_level=None)
db = conn.cursor()

def get_resort_conditions(id):
    db.execute('SELECT description FROM conditions WHERE resort=?', (id,))
    return db.fetchall()


def get_resort_metrics(id):
    db.execute('SELECT data FROM metrics WHERE resort=?', (id,))
    return db.fetchall()


def get_resort_id(resort):
    db.execute('SELECT id from resorts where name=?', (resort,))
    return int(db.fetchone()[0])


def get_resort_data(resort):
    rid = get_resort_id(resort)
    conditions = get_resort_conditions(rid)
    metrics = get_resort_metrics(rid)
    print(conditions)
    print(metrics)
