#!/bin/bash
# POST json file
curl -s -H "Content-Type: application/json" -H "Accept: application/json" -d"@$2" "$1" 
