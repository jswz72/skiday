import sqlite3
from definitions import DB_PATH, METRICS

conn = sqlite3.connect(DB_PATH, isolation_level=None)
db = conn.cursor()


def get_resort_conditions(r_id):
    """ Get most recent conditions for given resort
    r_id: int
    """
    db.execute('SELECT description, date FROM conditions WHERE resort=? ORDER BY date LIMIT 1', (r_id,))
    return db.fetchone()


def get_resort_metrics(r_id):
    """ Get most recent metrics of all types for given resort
    r_id: int
    """
    metrics = {}
    db.execute('SELECT id, type from metric_types')
    for mtype, desc in db.fetchall():
        db.execute('SELECT data FROM metrics WHERE resort=? AND metric=? ORDER BY date LIMIT 1 ', (r_id, mtype))
        metrics[desc] = db.fetchone()[0]
    return metrics


def get_resort_id(resort):
    """ Get id of resort
    resort: str
    """
    db.execute('SELECT id from resorts where name=?', (resort,))
    return int(db.fetchone()[0])


def get_resort_data(resort=None, id=None):
    """ Get most recent data from given resort
    resort: str
    """
    if resort:
        rid = get_resort_id(resort)
    else:
        rid = id
    conditions, timestamp = get_resort_conditions(rid)
    metrics = get_resort_metrics(rid)
    return {**metrics, 'conditions': conditions, 'timestamp': timestamp}


def get_all_resort_data():
    """ Get most recent data from all resorts """
    db.execute('SELECT id, display from resorts')
    resorts = db.fetchall()

    data = {}
    for r_id, display in resorts:
        data[display] = get_resort_data(id=r_id)
    return data



