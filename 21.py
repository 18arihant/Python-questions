class calculator:
    def __init__(self,number):
        self.number=number

    def cube(self):
        return (self.number)**3
    
    def square(self):
        return (self.number)**2
    
num=float(input("Enter a number:"))
a=calculator(num)
print(a.cube())
print(a.square())

    