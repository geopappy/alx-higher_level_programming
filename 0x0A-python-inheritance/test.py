#!/usr/bin/python3

class Animal():
    def __init__(self, name):
        self.name= name

class cat(Animal):
    def __init__(self):
        pass
cat_1 =  cat('bimb')
print(cat_1.name)
