#!/bin/bash

# Development: Set proxy to http://localhost:5000
./set-env.sh dev

# Run client
cd client
npm start
