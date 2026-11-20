class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pincode):
        self.name = name
        self.salary = salary
        self.pincode = pincode

p = Programmer("John", 50000, 123456)
print(p.name, p.salary, p.pincode, p.company)

r = Programmer("rohan", 50000, 123456)
print(r.name, r.salary, r.pincode, r.company)