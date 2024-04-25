#!/bin/bash
# get body size
curl -si "$1" | grep Content-Length | cut -d' ' -f2
