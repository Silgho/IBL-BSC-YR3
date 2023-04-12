from collections import defaultdict

shoppingList = defaultdict(int)
name = input("Input your name to continue, please : \n")
print("Write down your shopping list below, one item per line:")
while True:
    try:
        shopping = input().strip().lower()
        if not shopping:
            break
        shoppingList[shopping] += 1
    except EOFError:
        break

print("Here is your grocery list",name," : \n")
for shopping in sorted(shoppingList.keys()):
    count = shoppingList[shopping]
    print(f"{count} {shopping.upper()}")