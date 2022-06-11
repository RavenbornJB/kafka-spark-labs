FROM python:3.9-slim
RUN pip install --upgrade pip
RUN pip install kafka-python cassandra-driver

COPY receiver/receiver.py /opt/app/
COPY ./cassandra_client.py /opt/app/

ENTRYPOINT ["python", "/opt/app/receiver.py"]
