def inc_to_cm(inches):
    return inches * 2.54

n = int(input("Enter the number of inches: "))
print(f"{n} inches is equal to {inc_to_cm(n)} centimeters.")