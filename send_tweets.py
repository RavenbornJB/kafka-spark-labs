import csv
from kafka import KafkaProducer
from datetime import datetime
import time


def send_tweets(filename, producer):
    with open(filename) as f:
        csv_reader = csv.DictReader(f)

        for tweet in csv_reader:
            payload = [tweet['text'], tweet['author_id'], datetime.now().strftime("%d_%m_%Y_%H_%M_%S")]

            producer.send('tweets', str(payload).encode('utf-8'))
            time.sleep(1)


if __name__ == '__main__':
    prod = KafkaProducer(bootstrap_servers='kafka-server')

    send_tweets('/opt/app/data/twcs.csv', prod)

    prod.close()
