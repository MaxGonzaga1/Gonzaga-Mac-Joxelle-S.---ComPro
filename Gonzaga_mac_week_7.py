x = 300

def nearestNumber():
    num1 = int(input("Enter a number (1): "))
    num2 = int(input("Enter a number (2): "))
    num3 = int(input("Enter a number (3): "))

    # compute distances correctly
    d1 = abs(num1 - x)
    d2 = abs(num2 - x)
    d3 = abs(num3 - x)

    # find nearest
    if d1 <= d2 and d1 <= d3:
        print(f"{num1} is the nearest number.")
    elif d2 <= d1 and d2 <= d3:
        print(f"{num2} is the nearest number.")
    else:
        print(f"{num3} is the nearest number.")

nearestNumber()