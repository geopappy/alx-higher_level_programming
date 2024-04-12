#!/usr/bin/python3

class LockedClass:
    def __setattr__(self, name, value):
        if name != "first_name":
            raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'")
        else:
            self.__dict__[name] = value
