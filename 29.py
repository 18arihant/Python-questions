# coffee shop

class coffee:
    def menue(self):
        print("The choice are: latte, expresso and normal coffee")
        self.a=input("Enter your choice:")
    def amount(self):
        if self.a=="latte":
            print("pay Rs 60")
        elif self.a=="expresso":
            print("pay Rs 70")
        elif self.a=="coffee":
            print("pay Rs 50")
        else:
            print("wrong choice")

arihant=coffee()
arihant.menue()
arihant.amount()


