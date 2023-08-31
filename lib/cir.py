import ipdb
class Circle:
    def __init__(self, radius):
        self._radius = radius 
    
    @property
    def radius(self):
        print("Get radius")
        return self._radius
    
    @radius.setter
    def radius(self, value):
        print("Set radius")
        if value > 2:
            self._radius = value
        else:
            print("INVALID AMOUNT!")    

    @radius.deleter
    def radius(self):
        print("Delete radius")
        del self._radius

c = Circle(0)
print(c.radius) # 5

ipdb.set_trace()