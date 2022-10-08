#!/bin/bash
id=`sudo docker ps | grep servidorcasero | awk '{print $1;}'`;
sudo docker kill $id;
sudo docker rm $id;
sudo docker-compose up -d --build;
