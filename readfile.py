'''For a junior Engineer'''

with open("name.txt" , "r") as file: #The "r" is for reading the file
    lines = file.readlines()
    
for line in lines:
    print("Hello, " , line.rstrip()) #The .rstrip() is for removing spaces
    
    
'''For senior engineer'''

    
with open("name.txt" , "r") as file: #The "r" is for reading the file
    for line in file:
        print("Hello, " , line.rstrip()) #The .rstrip

