"""This is a programme to convert mass into energy"""
def mass_to_energy():
    user_name = input("To continue, Please enter your name : ")
    print("Hello " +user_name+ " , Welcome to mass to energy Converter")
    M = int(input("Enter your mass in Kilograms(Kg)  : "))
    C_squared =  (300000000**2)
    #energy = mass *c^2(speed of light squared)
    E = M * C_squared
    print("The Energy is ",E,"joules.")

mass_to_energy()