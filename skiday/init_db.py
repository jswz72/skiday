import sqlite3
import os
from definitions import DATA_PATH, RESORTS, METRICS

print(DATA_PATH)
if not os.path.exists(DATA_PATH):
    os.makedirs(DATA_PATH)


db = sqlite3.connect('../data/data.db')
cursor = db.cursor()
cursor.execute('CREATE TABLE resorts(id integer primary key, name varchar(255), display varchar(255));')
cursor.execute('CREATE TABLE conditions(resort integer not null, description varchar(255), date varchar(255), foreign key(resort) references resorts(id));')
cursor.execute('CREATE TABLE metric_types(id integer not null primary key, type varchar(255));')
cursor.execute('CREATE TABLE metrics(resort integer not null, metric integer not null, date varchar(255), data varchar(255), foreign key(resort) references resorts(id), foreign key(metric) references metric_types(id));')
cursor.execute('CREATE TABLE webpages(resort integer not null, url varchar(255), foreign key(resort) references resorts(id))')

for resort in RESORTS:
    cursor.execute('INSERT INTO resorts (name, display) VALUES (?, ?)', (resort['name'], resort['display']))
    cursor.execute('SELECT id from resorts where name=?', (resort['name'],))
    rid = int(cursor.fetchone()[0])
    cursor.execute('INSERT INTO webpages VALUES (?, ?)', (rid, resort['webpage']))

for metric in METRICS:
    cursor.execute('INSERT INTO metric_types (type) VALUES (?)', (metric,))

db.commit()
