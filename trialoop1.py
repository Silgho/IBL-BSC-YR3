class dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def set_age(self, age):
        self.age = age
        
d = dog("Tim", 54)
d.set_age(94)
print(d.get_name())
print(d.get_age())
