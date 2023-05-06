#create a class train that have cetain methods
class train:
    def __init__(self,seats,fare):
        self.seats=seats
        self.fare=fare

    def booking(self):
        self.seats-=1

    def status(self):
        print(self.seats)

    def fareinfo(self):
        print(self.fare)

a=train(21,450)
a.booking()
a.status()
a.fareinfo()
