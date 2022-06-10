#!/bin/bash

docker build -t sender .
docker run --name transaction-sender --network app-network --rm sender
