marks1 = int(input("Enter marks of student 1: "))
marks2 = int(input("Enter marks of student 2: "))   
marks3 = int(input("Enter marks of student 3: "))   
marks4 = int(input("Enter marks of student 4: "))

#check for total percentage

total_percentage = (marks1 + marks2 + marks3 + marks4) / 400*100
print("Total percentage is:", total_percentage)

if(total_percentage >= 40 and marks1>=33 and marks2>=33 and marks3>=33 and marks4>=33):
 print("Pass")

else:
    print("Fail")

    

