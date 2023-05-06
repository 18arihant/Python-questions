#create a class 2d vector and use it to create another clsss 3d vector
class Vector2d:
    def __init__(self,i,j):
        self.i=i
        self.j=j

    def printvector(self):
        print(self.i,"i +",self.j,"j")

class Vector3d(Vector2d):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k=k
    def printvector(self):
        print(self.i,"i +",self.j,"j +",self.k,"k")

v2=Vector2d(1,2)
v3=Vector3d(4,5,6)
v2.printvector()
v3.printvector()


        

