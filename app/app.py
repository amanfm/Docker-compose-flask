from typing import List, Dict
from flask import Flask
import mysql.connector
import json

app = Flask(__name__)


def full_name() -> List[Dict]:
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'aman'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM full_name')
    results = [{first_name: last_name} for (first_name, last_name) in cursor]
    cursor.close()
    connection.close()

    return results


@app.route('/')
def index() -> str:
    return json.dumps({'full_name': full_name()})


if __name__ == '__main__':
    app.run(host='0.0.0.0')
