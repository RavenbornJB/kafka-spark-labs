#!/bin/bash

docker build -f Dockerfile.sender -t send_tweets .
docker run --name tweet-sender --network kafka-network --rm send_tweets
