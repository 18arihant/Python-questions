# coffee shop

class coffee:
    def menue(self):
        print("The choice are: latte, expresso and normal coffee")
        self.a=input("Enter your choice:")
        self.b=int(input("Plese enter the quantity:"))

    def quantity(self,d,e,f):
        self.d=d
        self.e=e
        self.f=f
        print("The quantity of water sugar and coffee is",d, "gms",e, "grms",f, "gms")
    
    def amount(self):
        if self.a=="latte":
            print("pay Rs", 60*self.b)
        elif self.a=="expresso":
            print("pay Rs", 70*self.b)
        elif self.a=="coffee":
            print("pay Rs",50*self.b)
        else:
            print("wrong choice")

arihant=coffee()
arihant.menue()
arihant.quantity(50,50,50)
arihant.amount()


