import sqlite3
import datetime
from definitions import DB_PATH, METRICS

conn = sqlite3.connect(DB_PATH, isolation_level=None)
db = conn.cursor()


def get_resort_conditions(id):
    db.execute('SELECT description, date FROM conditions WHERE resort=? ORDER BY date LIMIT 1', (id,))
    return db.fetchone()


def get_resort_metrics(id):
    metrics = {}
    db.execute('SELECT id, type from metric_types')
    for mtype, desc in db.fetchall():
        db.execute('SELECT data FROM metrics WHERE resort=? AND metric=? ORDER BY date LIMIT 1 ', (id, mtype))
        metrics[desc] = db.fetchone()[0]
    return metrics


def get_resort_id(resort):
    db.execute('SELECT id from resorts where name=?', (resort,))
    return int(db.fetchone()[0])


def get_resort_data(resort):
    rid = get_resort_id(resort)
    conditions, timestamp = get_resort_conditions(rid)
    metrics = get_resort_metrics(rid)
    return {**metrics, 'conditions': conditions, 'timestamp': timestamp}
