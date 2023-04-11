x = int(input("Enter value of X : "))
y = int(input("Enter value of Y : "))

#function for addition
def addition():
    print(x + y)

addition()

# working with strings
def hello():
    print("Hello")

hello()

# working with strings with a parameter.
name = input("What is your name? ").strip() #we use .strip() to remove unnecesary space.
age = int(input("what is your age ? "))
def hello(z="World!",a="4.543 billion"):
    print("hello, ", z ," and your age is ", a ,"years")

hello(name, age)

#if you call the function without a parameter bacause the  we have value of z as "hey!" the value will be printed.
hello()


