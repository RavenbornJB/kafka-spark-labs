FROM python:3.9-slim
RUN pip install --upgrade pip
RUN pip install kafka-python

COPY ./sender.py /opt/app/
COPY ./data/PS_20174392719_1491204439457_log.csv /opt/app/data/

ENTRYPOINT ["python", "/opt/app/sender.py"]
