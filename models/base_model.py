#!/usr/bin/env python3
"""
This module contains class model that defines all common attributes for the
BaseModel class A class that is to act as a super class for all sub-
classes of the Airbnb
project
"""
import uuid
import datetime as dt


class BaseModel:
    """
    super class for the airbnb project with common classes
    """
    def __init__(self, *args, **kwargs):
        """
        Initialise attributes of the basemodules
            id, created_at and updated_at
        """
        if len(kwargs) > 0:  # instantiate model
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    tfmt = "%Y-%m-%dT%H:%M:%S.%f"
                    date_time = dt.datetime.strptime(value, tfmt)
                    setattr(self, key, date_time)
                else:
                    setattr(self, key, value)
        else:  # instantiate model by default
            self.id = str(uuid.uuid4())
            self.created_at = dt.datetime.now()
            self.updated_at = dt.datetime.now()

    def __str__(self):
        """
        print properties of class
        """
        return f"[{__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = dt.datetime.now()

    def to_dict(self):
        """
        return dictionary representation of class
        """
        dic = self.__dict__
        newdic = {}
        for key, value in dic.items():  # only attributes set are added to dict
            if value:
                newdic[key] = value
        newdic["__class__"] = __class__.__name__   # add classname to dict
        if 'created_at' in newdic:
            # replace created at value with iso formated string representation
            newdic['created_at'] = newdic['created_at'].isoformat(sep="T")
        if 'updated_at' in newdic:
            # replace update at value with iso formated string representation
            newdic['updated_at'] = newdic['updated_at'].isoformat(sep="T")
        return newdic
