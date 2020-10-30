#!/usr/bin/python3
"""
Define  BaseModel class
"""
import datetime
import uuid
import json


class BaseModel:
    """BaseModel class
    """
    def __init__(self):
        """Initialize BaseModel class objects.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def save(self):
        """Update the public instance attribute 'update_at' with the current
        datetime.
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """Return a dictionary containing all keys/value of __dict__ of the
        instance.
        """
        self.__dict__['__class__'] = BaseModel.__name__
        self.__dict__['created_at'] = self.__dict__['created_at'].isoformat()
        self.__dict__['updated_at'] = self.__dict__['updated_at'].isoformat()
        return self.__dict__

    def __str__(self):
        """String representation of BaseModel class

        Returns:
            [str]: representation of BaseModel class
        """
        return "[{}] ({}) {}".format(BaseModel.__name__,
                                     self.id, self.__dict__)
