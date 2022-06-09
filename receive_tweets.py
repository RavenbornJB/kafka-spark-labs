from kafka import KafkaConsumer
from ast import literal_eval
import csv


if __name__ == '__main__':
    cons = KafkaConsumer('tweets', bootstrap_servers='kafka-server')

    minute = None
    minute_tweets = []
    for message in cons:
        text, author_id, created_at = payload = literal_eval(message.value.decode('utf-8'))
        cur_minute = created_at[:-3]
        if not minute:  # init minute on first pass
            minute = cur_minute

        if minute != cur_minute:  # new minute
            with open(f'/tweet_logs/tweets_{minute}.csv', 'w') as f:
                csv_writer = csv.writer(f)
                csv_writer.writerow(['author_id', 'created_at', 'text'])
                csv_writer.writerows(minute_tweets)

                # update sentinel value
                minute = cur_minute
                minute_tweets = []

        minute_tweets.append(payload)

    cons.close()
