def value(salamu: str) -> int:
    salamuLower = salamu.lower()
    if salamuLower.startswith("hello"):
        return 0
    elif salamuLower.startswith("h"):
        return 20
    else:
        return 100


def main():
    salamu = input("Enter your salutation: ")
    print("The value of your salutation is: " + str(value(salamu)))


if __name__ == "__main__":
    main()