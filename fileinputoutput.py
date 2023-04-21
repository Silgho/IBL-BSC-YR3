name = input("What is your name : ")
'''
file = open("names.txt" , "a")      #inbuilt function to open the file document. the ("w" - rewrites & "a" - appends)
file.write(f"{name}\n")            #inbuilt function to write the input in a document.
file.close()                     #inbuilt function that closes the file document.
                                #with - is an inbuilt function that opens a file and closes it 
'''
with open("name.txt" , "a") as file:
    file.write(f"{name}\n") 
    
