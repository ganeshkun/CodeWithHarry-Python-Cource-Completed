f = open("file.text")

#lines = f.readlines()
#print(line, type(line))
# line0 = f.readline()
# print(line0, type(line0)) 

# line1 = f.readline()
# print(line1, type(line1)) 


# line2 = f.readline()
# print(line2, type(line2)) 

# line3 = f.readline()
# print(line3, type(line3)) 

# line4 = f.readline()
# print(line4 =="") 


line = f.readline()
while(line != ""):
    print(line, end="")
    line = f.readline()
f.close()