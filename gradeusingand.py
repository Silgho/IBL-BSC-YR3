#This ia a code which ones a score is entered the grade is printed.
score = int(input("Enter your score : "))

if score >= 90 and score <= 100:
    print("Grade : A ")
elif score >= 80 and score < 90:
    print("Grade : B ")
elif score >= 70 and score < 80:
    print("Grade : C ")
elif score >= 60 and score < 70:
    print("Grade : D ")
else:
    print("Grade : F ") 
    
#new way to code :     
#(Midlevel engineer)

if 90 <= score <= 100:
    print("Grade : A ")
if 80 <= score <= 90:
    print("Grade : B ")
if 70 <= score <= 80:
    print("Grade : C ")
if 60 <= score <= 70:
    print("Grade : D ")
else:
    print("Grade : F ") 
    
#new way to code :
# (Highlevel engineer)  

if score >= 90:
    print("Grade : A ")
if score >= 80:
    print("Grade : B ")
if score >= 70:
    print("Grade : C ")
if score >= 60:
    print("Grade : D ")
else:
    print("Grade : F ") 
    