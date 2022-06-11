from kafka import KafkaConsumer
from cassandra_client import CassandraClient
from ast import literal_eval


if __name__ == '__main__':
    client = CassandraClient('cassandra-server', 9042, 'lab')
    client.connect()

    cons = KafkaConsumer('fraud', bootstrap_servers='kafka-server')

    try:
        for message in cons:
            payload = literal_eval(message.value.decode('utf-8'))
            client.insert_transaction(payload)
    except KeyboardInterrupt as e:  # only way this is gonna end, other than the server going down
        client.shutdown()
        cons.close()
        raise e
