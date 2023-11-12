#!/bin/bash

# Development: Set proxy to http://localhost:5000
./set-env.sh dev

# Run server and client
python3 server/app/wsgi.py &
cd client
npm start
