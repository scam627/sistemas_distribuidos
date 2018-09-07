#!/bin/bash

screen -S server -d -m node server.js
sleep 1
screen -S client_1 -d -m node client.js
sleep 1
screen -S client_2 -d -m node client.js
sleep 1
screen -S client_3 -d -m node client.js
sleep 1
screen -S client_4 -d -m node client.js
sleep 1
screen -r sever