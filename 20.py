#to create a class that stores the information of some programmers
class programmer:
    def __init__(self,name,age,language):
        self.name=name
        self.age=age
        self.language=language

    def printobj(self):
        print("The name of the the programmer is",self.name)
        print("The age of the the programmer is",self.age)
        print("The language of the the programmer is",self.language)


Arihant=programmer("Arihant",19,"Python")
Arihant.printobj()

