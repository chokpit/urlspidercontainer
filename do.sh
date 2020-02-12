#!/bin/bash
docker-compose down -v
docker stop -qa $(docker container ls)
#docker image rm bs4container
docker build -t bs4container .
docker-compose up
