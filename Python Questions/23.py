#Example of a multi level inheritance and super() method
class Parent:
    a=4
    def __init__(self):
        print("Parent")

class Child1(Parent):
    b=5
    def __init__(self):
        print("child1") 
        super().__init__()

class Child2(Child1):
    c=9
    def __init__(self):
        print("child2")
        super().__init__()

ch=Child2()
print(ch.a)
print(ch.b)
print(ch.c)
