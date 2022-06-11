FROM python:3.9-slim
RUN pip install --upgrade pip
RUN pip install kafka-python

COPY sender/sender.py /opt/app/
COPY sender/data/data.csv /opt/app/data/

ENTRYPOINT ["python", "/opt/app/sender.py"]
