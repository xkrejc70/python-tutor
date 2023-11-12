#!/bin/bash

# Determine if it's a development environment or deployment
if [ "$1" == "dev" ]; then
    # Development: Set proxy to http://localhost:5000
    echo "Setting development proxy in package.json"
    sed -i 's|"proxy": "http://nginx:4000"|"proxy": "http://localhost:5000"|' client/package.json
else
    # Deployment: Set proxy to http://nginx:4000
    echo "Setting deployment proxy in package.json"
    sed -i 's|"proxy": "http://localhost:5000"|"proxy": "http://nginx:4000"|' client/package.json
fi