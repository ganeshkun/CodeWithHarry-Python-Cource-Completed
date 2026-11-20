
class employee:
    name= "Ganesh"
    language= "Python"
    Salary= 10000
    def getinfo(self):
        print(f"The language is {self.language}. The salary is {self.Salary}.")

    @staticmethod
    def greet():
        print("Good morning") 

harry = employee()

print (harry.name, harry.language)

Ganesh = employee()
Ganesh.language = "Java"
print (Ganesh.language, Ganesh.Salary) 
Ganesh.greet()
Ganesh.getinfo()
