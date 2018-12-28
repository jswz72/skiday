import sqlite3

db = sqlite3.connect('data.db')
cursor = db.cursor()
cursor.execute('CREATE TABLE resorts(id integer primary key, name varchar(255));')
cursor.execute('CREATE TABLE conditions(resort integer not null, description varchar(255), date text, foreign key(resort) references resorts(id));')
cursor.execute('CREATE TABLE metric_types(id integer not null primary key, type varchar(255));')
cursor.execute('CREATE TABLE metrics(resort integer not null, metric integer not null, date text, data integer, foreign key(resort) references resorts(id), foreign key(metric) references metric_types(id));')
cursor.execute('CREATE TABLE webpages(resort integer not null, url varchar(255), foreign key(resort) references resorts(id))')
db.commit()