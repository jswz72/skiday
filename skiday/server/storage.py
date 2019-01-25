import sqlite3
from definitions import DB_PATH

conn = sqlite3.connect(DB_PATH)
db = conn.cursor()

def write_resort_data(resort, data):
    pass

def get_url(resort):
    db.execute('SELECT id from resorts where name=?', (resort,))
    rid = db.fetchone()[0]
    db.execute('SELECT url from webpages where resort=?', (int(rid),))
    return db.fetchone()[0]

