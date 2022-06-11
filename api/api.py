from flask import Flask, request
from cassandra_client import CassandraClient
import json


app = Flask(__name__)


@app.route('/', methods=['POST'])
def api():
    if request.form['query_type'] == 'fraudulent':
        res = client.first_query(request.form['sid'])
    elif request.form['query_type'] == 'highest':
        res = client.second_query(request.form['sid'])
    elif request.form['query_type'] == 'date_sum':
        res = client.third_query(request.form['rid'], request.form['start_date'], request.form['end_date'])
    else:
        return 404

    return json.dumps(res, default=str)


if __name__ == '__main__':
    client = CassandraClient('cassandra-server', 9042, 'lab')
    client.connect()

    try:
        app.run(host='0.0.0.0', port=5050)
    except KeyboardInterrupt as e:
        client.shutdown()
        raise e
