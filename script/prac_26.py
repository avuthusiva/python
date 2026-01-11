from psycopg2 import connect
import json

file_path = '../docker/config.json'
with open(file_path, 'r') as file:
    config = json.load(file)
connection = connect(
    dbname=config['dbname'],
    user=config['username'],
    password=config['password'],
    host=config['host'],
    port=config['port'])
cur = connection.cursor()
sql = "select * from users;"
cur.execute(sql)
records = cur.fetchall()
for row in records:
    print(row)
print("Data retrieved successfully")
