#!/usr/bin/python3
"""serialize object"""
import json


def save_to_json_file(my_obj, filename):
    """write object to file using JSON"""
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
