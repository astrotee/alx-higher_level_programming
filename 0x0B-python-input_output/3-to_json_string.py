#!/usr/bin/python3
"""serialize object"""
import json


def to_json_string(my_obj):
    """object to JSON string"""
    return json.dumps(my_obj)
