#!/bin/bash

# Get the current year
YEAR=$(date +'%Y')

# Archive the logs
tar -czvf logs/logs_$YEAR.tar.gz logs/*.log

echo "Logs archived for the year $YEAR"
