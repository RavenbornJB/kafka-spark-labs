#!/bin/bash

docker stop kafka-server zookeeper-server cassandra-server
docker rm kafka-server zookeeper-server cassandra-server
docker network rm app-network
