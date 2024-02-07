#!/usr/bin/python3
"""deserialize object"""
import json


def load_from_json_file(filename):
    """load object from file using JSON"""
    with open(filename, 'r') as f:
        return json.load(f)
