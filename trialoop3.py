class pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old.")
        
    def speak(self):
        print("I don't know what to say!")

class cat(pet):  #the(pet) shows that the class cat inherits the pet class variables
    def __init__(self, name, age, color):
        super().__init__(name, age)         #inheritance of the class cat inherits the pet and adds to itself
        self.color = color
        
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")
        
    
    def speak(self):
        print("Meow")
class dog(pet):
    def speak(self):
        print("Bark")
        
class fish(pet):
    pass


d = dog("Tom",23)
d.show()
d.speak()
f = fish("Bubble", 12)
f.show()
f.speak()
c = cat("Pussi", 21 ,"White")
c.show()
c.speak()
p = pet("Tim", 18)
p.speak()
p.show()
