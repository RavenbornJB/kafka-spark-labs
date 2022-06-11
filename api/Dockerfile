FROM python:3.9-slim
RUN pip install --upgrade pip
RUN pip install flask cassandra-driver

COPY api/api.py /opt/app/
COPY ./cassandra_client.py /opt/app/

ENTRYPOINT ["python", "/opt/app/api.py"]
