#!/usr/bin/env python3
import ipdb
APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self):
        #self._name = name
        #self._breed = breed
        self.age = 0

    def get_name(self):
        print("retrieving name")
        return self._name

    def set_name(self,name):
        if (type(name) == str) and (len(name)>0):
            print("Valid string found")
            self._name = name
        else:
            print("Name must be string between 1 and 25 characters")

    def get_breed(self):
        print("Checking Breed")
        return self._breed

    def set_breed(self,breed):
        if breed in APPROVED_BREEDS:
            print("breed is valid")
        else:
            print("Invalid Breed!")    

    
    
    name = property(get_name,set_name,)
    breed = property(get_breed,set_breed,)        

#Bo = Dog(1234)

#print(Bo.name)

#ipdb.set_trace()