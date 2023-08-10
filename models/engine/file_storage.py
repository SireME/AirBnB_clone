#!/usr/bin/env python3
"""
This modlue contains a class FileStorage that serializes instances
to a JSON file and deserializes JSON file to instances
"""
import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """
    class for serialisation and deserilisation
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        this function returns dictionary objects
        representing an instnace
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        this method  sets in __objects the
        obj with key <obj class name>.id
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """
        this method serializes __objects to the
        JSON file (path: __file_path)
        """
        fname = FileStorage.__file_path
        data = FileStorage.__objects
        to_save = {}
        for key, obj in data.items():
            to_save[key] = obj.to_dict()
        with open(fname, "w", encoding="utf8") as f:
            json.dump(to_save, f, indent=4)

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ; otherwise, do
        nothing. If the file doesn’t exist, no exception should is raised)
        """
        try:
            fname = FileStorage.__file_path
            with open(fname, "r", encoding="utf8") as f:
                data = json.load(f)
                for key, value in data.items():
                    obj_name = value["__class__"]
                    del value["__class__"]
                    instance = globals()[obj_name](**value)
                    self.new(instance)
                    # self.new(eval(obj_name)(**value)) alterntive above method
        except FileNotFoundError:
            pass
