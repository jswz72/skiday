import sqlite3

conn = sqlite3.connect('../data/db')
db = conn.cursor()

def write_resort_data(data):
    #get ids of metric types and write metric with date
    pass

def get_url(resort):
    db.execute('SELECT id from resorts where name=?', (resort,))
    rid = db.fetchone()[0]
    db.execute('SELECT url from webpages where resort=?', (int(rid),))
    return db.fetchone()[0]

