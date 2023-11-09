#!/bin/bash

python3 ../src/grpc_server.py &
python3 ../src/http_server.py
