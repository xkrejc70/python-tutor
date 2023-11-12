#!/bin/bash

# Development: Set proxy to http://localhost:5000
echo "Setting development proxy in package.json"
sed -i 's|"proxy": "http://nginx:4000"|"proxy": "http://localhost:5000"|' client/package.json

python3 server/app/wsgi.py &
cd client
npm start
