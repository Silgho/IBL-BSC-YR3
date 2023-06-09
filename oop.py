class Student:
    def __init__(self, name, estates, course):
        if not name:
            raise ValueError("Please provide your name ")
        
        self.name = None
        self.course = course
        self.estates = estates
        
    def __str__(self):
        return f"{self.name} is from {self.estates} and is doing {self.course}"
    
    #getter for the estate
    @property
    def estates(self):
        return self.estates  
    
    #setter for the estate
    @estates.setter
    def estates(self, estates):
        if estates not in ["Tena", "South B", "Umoja 1", "Umoja 2" , "Karen"]:
            raise ValueError("Invalid Estate")
        self._estates = estates
        
def main():
        student = get_student()
        print(student)
        
def get_student():
        name = input("what is your name? ").strip()
        estates = input("what is your estate? ").strip()
        course = input("what is your course? ").strip()
        return Student(name, estates, course)
    
if __name__ == "__main__":
    main()
        