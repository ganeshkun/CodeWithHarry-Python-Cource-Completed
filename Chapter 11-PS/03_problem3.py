class Employee:
   salary = 50000
   increment = 4000
   @property
   def salaray_after_increment(self):
       return self.salary + self.salary * self.increment/100
   @salaray_after_increment.setter
   def salaray_after_increment(self, salary):
      self.increment = ((salary/self.salary) -1)*100



e = Employee()
# print(e.salaray_after_increment)
e.salaray_after_increment = 60000
print(e.increment)