class Calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
       print(self.n * self.n)

    def cube(self):
      print(self.n * self.n * self.n)

    def squareroot(self):
     print(self.n ** 0.5)
    @staticmethod
    def hello():
        print("Hello World")



a = Calculator(5)
a.square()
a.cube()
a.squareroot()  
a.hello()