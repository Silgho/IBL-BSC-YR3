"""
This is a python programme that duplicates tasks uploaded by the user

"""
def main():
    x=number_of_times()
    task = your_task()
    print("Your duplicates are : \n")
    for _ in range(x):
            
            print(task)

def number_of_times():
    x = int(input("Number of duplications : "))
    return (x)

def your_task():
    task = input("Enter Task "+user_name()+"\n Enter... ")
    return (task)

def user_name():
    name = input("What is your name? ")
    return (name)

main()

