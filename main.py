import sqlite3, requests
conn = sqlite3.connect('./data/data.db')
db = conn.cursor()
conn.row_factory = lambda cursor, row: row[0]

def get_webpage(resort):
    db.execute('SELECT id from resorts where name=?', (resort,))
    rid = db.fetchone()[0]
    db.execute('SELECT url from webpages where resort=?', (int(rid),))
    url = db.fetchone()[0]
    r = requests.get(url)
    return r.text

print(get_webpage('Cannon'))
