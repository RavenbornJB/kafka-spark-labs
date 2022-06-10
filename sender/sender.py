import csv
from kafka import KafkaProducer

from datetime import timedelta
from datetime import date

import random
import time


def send_messages(filename, producer):
    with open(filename) as f:
        csv_reader = csv.DictReader(f)

        for transaction in csv_reader:
            transaction_date = date.today() - timedelta(days=random.randint(0, 30))

            payload = [
                transaction['nameOrig'],
                transaction['nameDest'],
                transaction['amount'],
                transaction_date.strftime("%Y-%m-%d"),
                transaction['isFraud']
            ]

            producer.send('fraud', str(payload).encode('utf-8'))
            time.sleep(1)


if __name__ == '__main__':
    prod = KafkaProducer(bootstrap_servers='kafka-server')

    send_messages('/opt/app/data/data.csv', prod)

    prod.close()
