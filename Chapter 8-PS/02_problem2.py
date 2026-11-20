def f_to_celsius(f):
    return (f - 32) * 5/9

f = int(input("Enter temp: "))
print("The temperature in Celsius is:", round(f_to_celsius(f),2))