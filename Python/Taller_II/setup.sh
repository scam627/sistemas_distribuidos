#!bin/bash

python server_sum.py > /dev/null &
python server_res.py > /dev/null &
python server_mul.py > /dev/null &
python server_div.py > /dev/null &
python server_pot.py > /dev/null &
python server_log.py > /dev/null &
python server_rad.py > /dev/null &
python proxy.py >> trash.txt &