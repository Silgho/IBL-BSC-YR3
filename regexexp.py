import re 
#for validation of emails.
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  
def check():
    email =  input("enter your email address: ")
    if(re.search(regex,email)):   
        print("Valid Email")   
    else:   
        print("Invalid Email")   
        
check()
