import ipdb
import re

class Dog:
    species = 'mammal'

    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,value):
        if type(value) != str:
            raise TypeError("Name must be a string")
        self._name = value

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self,value):
        if value < 0:
            raise ValueError("age must be an integer")
        self._age = value

class Citizen:
    def __init__(self, id, name, email, age):
        self._id = id
        self.name = name
        self.email = email
        self.age = age

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) > 20:
            raise ValueError("Name cannot exceed 20 characters.")
        self._name = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        regex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
        if not re.match(regex, value):
            raise ValueError("It's not an email address.")
        self._email = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative.")
        self._age = value



ipdb.set_trace()