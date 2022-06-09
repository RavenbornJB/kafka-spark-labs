#!/bin/bash

docker build -t send_tweets .
docker run --network kafka-network --rm send_tweets