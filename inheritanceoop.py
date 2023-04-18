class Firstname:
    def __init__(self, name):
        if not name:
            raise ValueError("No name specified")
        self.name = name
        
class Student(Firstname):
    def __init__(self, name, course):
        super().__init__(name)
        self.course = course
        
def main():
    student
Student = Student("Bostone", "Information Science")
print(Student)