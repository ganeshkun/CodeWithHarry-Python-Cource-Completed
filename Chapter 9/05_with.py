f = open("file.text")

print(f.read())

f.close()

# the same statement can be written using with statement as follows:

with open("file.text") as f:
    print(f.read())

# u dont have to close the file when using with statement, it will automatically close the file after the block of code is executed.