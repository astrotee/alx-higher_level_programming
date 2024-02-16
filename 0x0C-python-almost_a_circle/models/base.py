#!/usr/bin/python3
"""Base class"""
import json
import os


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

    @staticmethod
    def from_json_string(json_string):
        """deserialize JSON string"""
        if json_string is None:
            json_string = "[]"

        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        if list_objs is None or not issubclass(cls, Base):
            list_dicts = []
        else:
            list_dicts = [x.to_dictionary() for x in list_objs]

        with open(f"{cls.__name__}.json", "w") as f:
            f.write(Base.to_json_string(list_dicts))

    @classmethod
    def create(cls, **dictionary):
        """create instance with given attributes"""
        if issubclass(cls, Base):
            o = cls(1, dictionary.get("height", 0))
            o.update(**dictionary)
        else:
            o = cls(id=dictionary.get("id", None))
        return o

    @classmethod
    def load_from_file(cls):
        """create instances form file"""
        list_objs = []
        if not os.path.exists(f"{cls.__name__}.json"):
            return []
        with open(f"{cls.__name__}.json") as f:
            for d in Base.from_json_string(f.read()):
                list_objs.append(cls.create(**d))
            return list_objs

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """writes the CSV string representation of list_objs to a file"""
        if list_objs is None or not issubclass(cls, Base):
            list_objs = []

        with open(f"{cls.__name__}.csv", "w") as f:
            for obj in list_objs:
                f.write(f"{obj.id},")
                if "size" in obj.to_dictionary():
                    f.write(f"{obj.size},")
                else:
                    f.write(f"{obj.width},{obj.height},")
                f.write(f"{obj.x},{obj.y}\n")

    @classmethod
    def load_from_file_csv(cls):
        """create instances form CSV file"""
        keys = [['id', 'size', 'x', 'y'],
                ['id', 'width', 'height', 'x', 'y']
                ]
        list_objs = []
        if not os.path.exists(f"{cls.__name__}.csv"):
            return []
        with open(f"{cls.__name__}.csv") as f:
            for line in f.readlines():
                values = list(map(int, line.strip().split(',')))
                if len(values) == 4:
                    d = dict(zip(keys[0], values))
                else:
                    d = dict(zip(keys[1], values))
                list_objs.append(cls.create(**d))
            return list_objs
