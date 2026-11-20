
class employee:
    name= "Ganesh"
    language= "Python"
    Salary= 10000
    def getinfo(self):
        print(f"The language is {self.language}. The salary is {self.Salary}.")

    def __init__(self, name, salary, language): #dunder method which is automatically called when an object is created. It is used to initialize the object.
        self.name = name
        self.Salary = salary
        self.language = language
        print(f"I am creating an object")
 
    @staticmethod
    def greet():
        print("Good morning") 



Ganesh = employee("Kunwar", 20000, "Java")
# Ganesh.name = "Ganesh Kunwar"
print(Ganesh.name, Ganesh.language, Ganesh.Salary)
