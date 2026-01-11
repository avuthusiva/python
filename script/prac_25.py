import psycopg2
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
cur.execute('SELECT version();')
record = cur.fetchone()
print(f'You are connected to - {record}\n')
print("Connection established successfully")