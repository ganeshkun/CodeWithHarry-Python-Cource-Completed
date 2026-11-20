class vector:
    def __init__(self,l):
      self.l = l

    def __len__(self):
        return len(self.l)
    
v1 = vector([2, 3, 6])

print(len(v1))  # Output: 3