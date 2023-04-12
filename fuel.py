while True:
    try:
        fraction = input("Enter level of fuel as a fraction (X/Y): ")
        a, b = fraction.split('/')
        a, b = int(a), int(b)
        if b == 0 or a > b:
            raise ValueError
        break
    except (ValueError, ZeroDivisionError):
        print("Sorry! Invalid input. Please try again...")

percentage = round(a / b * 100)
if percentage <= 1:
    print("E")
elif percentage >= 99:
    print("F")
else:
    print(f"{percentage}%")