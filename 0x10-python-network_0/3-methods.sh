#!/bin/bash
# get body size
curl -sI "$1" | grep Allow | cut -d' ' -f2-
