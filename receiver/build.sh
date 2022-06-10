#!/bin/bash

docker build -t receive_tweets .
docker run --name tweet-receiver --network kafka-network --rm receive_tweets
