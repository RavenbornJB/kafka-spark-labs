#!/bin/bash

docker build -f Dockerfile -t receiver .
docker run --name transaction-receiver --network app-network --rm receiver
