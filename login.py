class login():
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
class User(login):
    def __init__(self, username, password):
        super().__init__(username, password)
        
        self.Firstname = Firstname
        self.last_name = last_name
        self.email_address = email_address
        
    def __str__(self):
        return f"your name is {self.Firstname} {last_name} and your password is {self.password} and he email address is {self.email_address}"
    
def main():
    user = User("Bostone12","TUK001" "Ochieng' ", "Kelvin", "ochie@gmail.com")
    print(user)
    
if __name__ == "__main__":
    main()