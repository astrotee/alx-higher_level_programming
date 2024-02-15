#!/usr/bin/python3
"""Base class"""
import json


class Base:
    """Base class for this project"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """JSON string representation"""
        if list_dictionaries in (None, []):
            return "[]"
        return json.dumps(list_dictionaries)
