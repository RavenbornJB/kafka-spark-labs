#!/bin/bash

docker build -f Dockerfile.sender -t send_tweets .
docker run --network kafka-network --rm send_tweets
