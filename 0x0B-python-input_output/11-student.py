#!/usr/bin/python3
"""module defines student class"""


class Student():
    """Students class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            attrs = ['first_name', 'last_name', 'age']
        return {key: value for key, value in self.__dict__.items() if key in
                attrs}
    def reload_from_json(self, json):
        for k, v in json.items():
            setattr(self, k, v)
