from collections import defaultdict

# Initialize an empty dictionary to store item counts
shoppingList = defaultdict(int)

# Prompt the user for input
print("Write down your shopping list below, one item per line:")
while True:
    try:
        shopping = input().strip().lower()
        if not shopping:
            break
        shoppingList[shopping] += 1
    except EOFError:
        break

# Print the grocery list
print("Here is your grocery list:")
for shopping in sorted(shoppingList.keys()):
    count = shoppingList[shopping]
    print(f"{count} {shopping.upper()}")