class Employee:
    company = "Microsoft"
    name = "John"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.name}")

class coder:
   language = "Python"
   def printlanguage(self):
       print(f"The name is {self.company} and the name is {self.name}") 


# class Programmer:
#     company = "ITC"
#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}")

#     def showlanguage(self):
#         print(f"The name is {self.name} and the salary is {self.language}")

class Programmer(Employee, coder):
    company = "ITC"
    def showlanguage(self):
     print(f"The name is {self.company} and the language is {self.language}")

a = Employee()
b = Programmer()

b.show()
b.printlanguage()
b.showlanguage()
