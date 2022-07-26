class Flyable:
    def __init__(self, name):
        self.name = name
        
    def fly(self):
        print(f"{self.name} is flying")
        
    def __str__(self):
        return "fly"
    
class Swimable:
    def __init__(self, water):
        self.water = water
        
    def swim(self):
        print(f"{self.water} is cool")
        
    def __str__(self):
        return "olol"
    
class Duck(Flyable, Swimable):
    def __init__(self, name,water, place):
        Flyable.__init__(self,name)
        Swimable.__init__(self,water)
        self.place = place
        
    def fly(self):
        return super().fly()
    
    def swim(self):
        return super().swim()
    
duck = Duck("Don", 'sea', 'KZ')

duck.fly()
duck.swim()