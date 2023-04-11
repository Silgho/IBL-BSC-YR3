"""This is a programme to convert uppercase to lowercase"""
def To_Lower_Case():
    name = user_name()
    print("Hello " +name+ " , Welcome to Lowercase Converter\n")
    task = user_task()
    #we use .strip() to remove unnecessary spaces
    out_put = task.lower()
    #we use .lower() to convert upper case to lowercase
    print("\nProblem has been solved and the solution is : \n")
    print(out_put)
    
def user_name():
    name = input("What is your name? ")
    return (name)
def user_task():
    task = input("Enter your task  : \n")
    return (task)

To_Lower_Case() 