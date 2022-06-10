import csv
from kafka import KafkaProducer
from datetime import datetime
import time


def send_messages(filename, producer):
    with open(filename) as f:
        csv_reader = csv.DictReader(f)

        for transaction in csv_reader:
            producer.send('tweets', str(payload).encode('utf-8'))
            time.sleep(1)


if __name__ == '__main__':
    prod = KafkaProducer(bootstrap_servers='kafka-server')

    send_messages('/opt/app/data/PS_20174392719_1491204439457_log.csv', prod)

    prod.close()
