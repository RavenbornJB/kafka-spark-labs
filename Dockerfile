FROM python:3.9-slim
RUN pip install --upgrade pip
RUN pip install kafka-python

COPY ./send_tweets.py /opt/app/
COPY ./data/twcs.csv /opt/app/data/

ENTRYPOINT ["python", "/opt/app/send_tweets.py"]
