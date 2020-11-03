#!/usr/bin/python3
"""
Define  FileStorage class
"""
import json
import os

from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage:
    """FileStorage class
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """returns the dictionary.
        """
        return type(self).__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id

        Args:
            obj (BaseModel): BaseModel to set in __objects.
        """
        key = type(obj).__name__ + '.' + obj.id
        type(self).__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file.
        """
        dict_objs = {obj_id: obj.to_dict()
                     for obj_id, obj in type(self).__objects.items()}
        with open(type(self).__file_path, mode='w') as file:
            json.dump(dict_objs, file)

    def reload(self):
        """deserializes the JSON file to __objects.
        """
        if os.path.isfile(type(self).__file_path):
            with open(type(self).__file_path, mode='r') as fp:
                dict_of_dicts = json.load(fp)
                for _dict in dict_of_dicts.values():
                    cls_name = _dict['__class__']
                    self.new(eval(cls_name)(**_dict))
