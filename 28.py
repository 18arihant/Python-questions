# to add and multipy 2 vectors

class  vector:
    def __init__(self,l1):
        self.l1=l1
        self.data=l1

    def __add__(self,obj):
        mylist=[]
        for i in range(len(obj.data)):
            mylist.append(self.data[i]+obj.data[i])

        return(vector(mylist))
    
    def __mul__(self,obj):
        dot=0
        for i in range(len(obj.data)):
            dot+=(self.data[i]*obj.data[i])
        return dot
    
v1=vector([1,2,3])
v2=vector([2,3,4])
v3=v1+v2
v4=v1*v2
print(v3.data)  
print(v4)
 
        