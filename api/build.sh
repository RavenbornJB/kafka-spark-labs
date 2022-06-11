#! /bin/bash

docker build -f api/Dockerfile -t api .
docker run --name transaction-api --network app-network -p 5050:5050 --rm api
