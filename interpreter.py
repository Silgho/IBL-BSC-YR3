print("Welcome to my Calculator programme! ")
print("Our Operators are: ")
print("+ for Addition, * for Multiplication,/ for Division,and - for Minus ")
def my_calc():
    A = int(input("Enter the first number: "))
    B = input("Enter the operator(+,-,/,*,): ")
    C = int(input("Enter the second number: "))
    
    if B == "+":
        print(A + C)
    elif B == "-":
        print(A - C) 
    elif B == "*":
        print(A * C)
    elif B == "/":
        print(A / C)
    else:
        print("Invalid operator")
        
my_calc()