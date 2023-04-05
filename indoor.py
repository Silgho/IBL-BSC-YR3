"""This is a programme to convert uppercase to lowercase"""
def To_Lower_Case():
    user_name = input("To continue, Please enter your name : ")
    user_name = user_name.strip()
    #we use .strip() to remove unnecessary spaces
    print("Hello " +user_name+ " , Welcome to Lowercase Converter")
    user_input = input("Enter your task  : ")
    out_put = user_input.lower()
    #we use .lower() to convert uppercase to lowercase
    print("Problem has been solved and the solution is : ")
    print(out_put)

To_Lower_Case() 