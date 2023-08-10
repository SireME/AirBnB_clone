#!/usr/bin/python3
"""
This module defines a FileStorage class to serialize instances
and store them in a JSON file.
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """
    This class serializes instances to a JSON file and deserializes
    JSON file to instances.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        json_dict = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(json_dict, file)

    def reload(self):
        try:
            with open(FileStorage.__file_path, 'r') as file:
                json_dict = json.load(file)
                for key, value in json_dict.items():
                    cls_name = value['__class__']
                    obj = eval(cls_name + "(**value)")
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass

