import ipdb

inputed = "Kimani"

class Human:
     # Variables set outside the scope of any methods are called class attributes
     # All members of the human class have the same species
     # Doing this is more effective than setting the species of the class everytime
     # On instantiation
    species = "Homo sapiens"   
    def __init__(self, name):
        # Name is an instance attribute meaning it can only be called once an
        # instance (Object) is created
        self.name = name

        #Properties in python are attributes that are controlled by methods

        self._age = 0                                       #the underscore in _age tells programmers that this is a private method


    def run():
        return "run"

    #We have to protect our object's attributes and methods since
    #some methods are meant to be accessed by different roles

    #Public members methods are available to anyone that can access the class
    #Private members are only available to the class that instantiated them
    #Protected members are available to the class that instantiated them AND
    #any object that inherits from that class

    def get_age(self):
        print("Retrieving age.")
        return self._age
        print(Kim._age)

    def set_age(self,age):
        if (type(age)in (int,float)) and (0 <= age <= 120):
            print(f"setting age to {age}")
            self._age = age
        else:
            print("Age must be a number between 0 and 120")    

    age = property(get_age, set_age,)                   #The property function. Its attributes are set by the get_age and set_age m
                                                        #Use property functions when you need to validate inputs

#We DO NOT WANT THIS:

guido = Human("Guido")

#An object should NOT be able to modify its established class attribute!

guido.species = "Python programmer"

#A better way:

        
getattr(guido,"species")                            #The getaatrr() command retrieves the value of a command

setattr(guido, "species", "C programmer")           #The setattr() command changes the value of an attribute 

#the attr() are useful for their ability to set or delete attributes who's names are unknown


print(guido.species)


Kim = Human("Kimani")

ipdb.set_trace()