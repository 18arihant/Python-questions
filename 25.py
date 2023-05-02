#Create a class that store a list and find the average of minimum and maximum value
class list():
    def __init__(self,a):
        self.a=a

    def avg(self):
        
        self.minimum=min(self.a)
        self.maximum=max(self.a)
        return (self.minimum + self.maximum)/2
    

b=list([100,200,50,250])
print(b.avg())



        
