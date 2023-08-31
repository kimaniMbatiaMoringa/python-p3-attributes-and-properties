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
    def __init__(self,name='',breed='none'):
            self.name = name
            self.breed = breed
    
    #@property
    #def name(self):
    #    return self._name
    
    #@name.setter
    #def name(self,value):
    #    if (type(value) == str) and (len(value)>0):
    #        #print("Valid string found")
    #        self._name = value
    #    else:
    #        print("Name must be string between 1 and 25 characters")


    def get_name(self):
         return self._name
    
    def set_name(self, value):
        if (type(value) == str) and (len(value)>0):
            #print("Valid string found")
            if len(value)>25:
                 print("Name must be string between 1 and 25 characters.")
            self._name = value
        else:
            print("Name must be string between 1 and 25 characters.")

    
    def get_breed(self):
         return self._breed

    def set_breed(self,breed):
        if breed in APPROVED_BREEDS:
            print("breed is valid")
        else:
            print("Invalid Breed!")    

    name = property(fget=get_name,fset=set_name)
    breed = property(fget=get_breed,fset=set_breed)        

#Bo = Dog(1234)

#print(Bo.name)

ipdb.set_trace()