def main():
    x = int(input("What is the value of X ? "))
    if mod(x): 
        print("Even")
    else:
        print("Odd")    

#junior engineer functions.  
def mod(n):
    if n % 2 == 0:
        return True
    else:
        return False      
"""   
as a middle level Engineer you would prefer the above function 
def mod(n):
    
    return True if n % 2 == 0 else False  
    
"""       

"""   
as a senior level Engineer you would prefer the above function 
def mod(n):
    
    return n % 2 == 0  
    
"""     
    
main()    