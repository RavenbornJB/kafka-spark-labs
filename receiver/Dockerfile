FROM python:3.9-slim
RUN pip install --upgrade pip
RUN pip install kafka-python

COPY ./receiver.py /opt/app/

ENTRYPOINT ["python", "/opt/app/receiver.py"]
