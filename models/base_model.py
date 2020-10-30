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
    def __init__(self, *args, **kwargs):
        """Initialize BaseModel class objects.
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
        else:
            for key in kwargs:
                if key != '__class__':
                    if key in ('created_at', 'updated_at'):
                        self.__dict__[key] = datetime.datetime.strptime(kwargs[key],
                                                                        '%Y-%m-%dT%H:%M:%S.%f')
                    else:
                        self.__dict__[key] = kwargs[key]

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
