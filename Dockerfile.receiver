FROM python:3.9-slim
RUN pip install --upgrade pip
RUN pip install kafka-python

RUN mkdir /tweet_logs

COPY ./receive_tweets.py /opt/app/

ENTRYPOINT ["python", "/opt/app/receive_tweets.py"]
