print("Enter a salutation in the space provided below: ")
txt = input("Here : ")

if txt.lower().startswith("hello"):
    print("$0.0")
elif txt.lower().startswith("h"):
    print("$20.0")
else:
    print("$100.0")       