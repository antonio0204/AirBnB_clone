#!/usr/bin/python3
"""
Define  BaseModel class
"""
import models
from datetime import datetime
import uuid
import json


class BaseModel:
    """BaseModel class
    """

    def __init__(self, *args, **kwargs):
        """Initialize BaseModel class objects.
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for key in kwargs:
                if key != '__class__':
                    if key in ('created_at', 'updated_at'):
                        date_obj = datetime.strptime(kwargs[key],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
                        self.__dict__[key] = date_obj
                    else:
                        self.__dict__[key] = kwargs[key]

    def save(self):
        """Update the public instance attribute 'update_at' with the current
        datetime.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return a dictionary containing all keys/value of __dict__ of the
        instance.
        """
        _dict = self.__dict__.copy()
        _dict["created_at"] = self.created_at.isoformat()
        _dict["updated_at"] = self.updated_at.isoformat()
        _dict["__class__"] = type(self).__name__
        return _dict

    def __str__(self):
        """String representation of BaseModel class

        Returns:
            [str]: representation of BaseModel class
        """
        return "[{}] ({}) {}".format(type(self).__name__,
                                     self.id, self.__dict__)
