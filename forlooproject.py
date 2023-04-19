'''
#for loop syntax :

for element in sequence:
    # for statement code block
else: # optional
    # else block code


'''

t = (1,2,3,4,5,6,7,8,9,10)

for i in t:
    print(i)
    
fruits = ["apple", "banana", "Grapes","Mangoes", "oranges"]

for fruit in fruits:
    print(fruit)
    
num_dict = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five"}

for k, v in num_dict.items():
    print(f"{k} = {v}")