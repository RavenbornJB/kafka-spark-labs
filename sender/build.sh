#!/bin/bash

docker build -f sender/Dockerfile -t send_tweets .
docker run --name tweet-sender --network kafka-network --rm send_tweets
