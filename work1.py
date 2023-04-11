 #functions in python programming
 # eg: print() round() input()
"""
def greet(first_name, second_name):
    print(f"Hi {first_name} {second_name}")
    print ("Welcome on board")
    
greet("Amos")

the above is a function that ones called it is executed
"""
'''
int() -> this function is used to convert into an integer.
float() -> this function is used to convert into a float.
ord() -> this function is used to convert character to integer.
hex() -> this function is used to convert integer to hexadecimal string.
oct() -> this function is used to convert integer to octal string.

        BELOW IS AN EXAMPLE OF A PYTHON PROGRAM USING FUNCTIONS
        
        The code below asks a user to input numbers then it adds up or multiply 
        those number, depending with the choice given by the user
        
        super additional or multiplicational calculator:  
'''

def suma():
    number_of_time = int(input("Number of entries : "))
    numbers = []
    for _ in range(number_of_time):
        numbers.append(int(input("numbers: ")))
    return numbers

def add():
    numbers = suma()
    sum_of_elements = sum(numbers)
        
    print("The sum is : ",sum_of_elements)
    
def multiply():
    numbers = suma()    
    sum_of_elements = 1
    for number in numbers:
        sum_of_elements = sum_of_elements * number
        
    print("The product is :",sum_of_elements)
    
def rep():
    x = int(input("for addition choose 1 and multiplications choose 2 back 0  \n"))
    if x == 1:
        add()
    elif x == 2:
        multiply()
    elif x == 0:
        rep()
        rep()
    else:
        print("Invalid input \n")
        
    
    
    
    
def main():
    print("SILGHO MULTI-ADDITIONAL CALCULATOR\n")
    name = input("Please, input you name to continue...\n")
    print("loading...\n")
    print("Hello "+name+" Welcome to maths corner...\n")
    x = int(input("for addition choose 1 and multiplications choose 2 back 0 \n"))
    if x == 1:
        add()
        rep()
    elif x == 2:
        multiply()
        rep()
    elif x == 0:
        rep()
        rep()
    else:
        print("Invalid input \n")
        rep()

    
    
main()