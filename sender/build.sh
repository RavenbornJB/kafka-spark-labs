#! /bin/bash

docker build -f sender/Dockerfile -t sender .
docker run --name transaction-sender --network app-network --rm sender
