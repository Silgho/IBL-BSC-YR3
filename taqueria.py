
menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

totalCost = 0.0
while True:
    try:
        item = input("Input an item: ").title()
        if item not in menu:
            continue
        price = menu[item]
        totalCost += price
        print(f"${totalCost:.2f}")
    except EOFError:
        break