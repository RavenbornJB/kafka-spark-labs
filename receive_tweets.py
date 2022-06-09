from kafka import KafkaConsumer
from ast import literal_eval
import csv


if __name__ == '__main__':
    cons = KafkaConsumer('tweets', bootstrap_servers='kafka-server')

    for message in cons:
        text, author_id, datetime = literal_eval(message.decode('utf-8'))
