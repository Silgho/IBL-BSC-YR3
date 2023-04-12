def vowelRemover(text):
    
    vowels = "AEIOUaeiou"
    for vowel in vowels:
        txt = txt.replace(vowel, "")
    return txt

txt = input("Please input your task : \n")
vowelRemovedTxt = vowelRemover(txt)
print(vowelRemovedTxt)