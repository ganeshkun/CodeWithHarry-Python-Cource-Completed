class TwoDVector:
    def __init__(self,i,j):
        self.i = i
        self.j = j

    def show(self):
        print(f"i: {self.i}, j: {self.j},")

class ThreeDVector(TwoDVector):
    def __init__(self,i, j, k):
        super().__init__(i, j)
        self.k = k
        
    def show(self):
      print(f"i: {self.i}, j: {self.j}, k: {self.k}")
        

o = TwoDVector(1, 2)
o.show()
n = ThreeDVector(1, 2, 3)
n.show()    
