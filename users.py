class user:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        
    def show_users(self):
        print(f"user name : {self.username}\n Email : {self.email}\n password : {self.password}")

class staff(user):
    def __init__(self, username, email, password, designation):
        super().__init__(username, email, password)
        self.designation = designation
        
        
    def show_users(self):
        print(f"I am {self.username}, my email is {self.email} and I am the {self.designation} of SilghoTech ltd")
class student(user):
    def __init__(self, username, email, password, course):
        super().__init__(username, email, password)
        self.course = course
        
    def show_users(self):
        print(f"My name is {self.username} and my email is {self.email} pursuing a bachelor of science in {self.course}.")
        
        
A = staff("Kioko", "k1@gmail.com", "K12345.", "Principal")
B = student("Samuel","SMK@gmail.com", "smk12345.", "Computer Science")
A.show_users()
B.show_users()