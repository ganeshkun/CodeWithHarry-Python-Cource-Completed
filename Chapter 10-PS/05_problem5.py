from random import randint


class Train:
    def __init__(self, trainno):
        self.trainno = trainno
    def book(self, trainno, fro, to):
        print(f"Your ticket is booked from {fro} to {to} in train number {trainno}")
    def getStatus(self, trainno):
        print(f"Train number {trainno} is on time")

    def getfare(self, trainno, fro, to):
        print(f"Your fare from {fro} to {to} in train number {trainno} is {randint(222,5555)}")


t = Train(12399)
t.book(12399, "Rampur", "Delhi")
t.getStatus(12399)
t.getfare(12399, "Rampur", "Delhi") 
