#!/bin/bash

docker build -t send_tweets .
docker run --name tweet-sender --network kafka-network --rm send_tweets
