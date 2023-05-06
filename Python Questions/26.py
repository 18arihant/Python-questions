# to create a class and add salary and increment  properties to it

class Employee:
    def __init__(self,salary,increment):
        self.salary=salary
        self.increment=increment

    @property
    def salaryafterincrement(self):
        return (self.salary + ((self.salary) * (self.increment)))
    
    @salaryafterincrement.setter
    def salaryafterincrement(self):
        self.salary=(self.salary + ((self.salary) * (self.increment)))
    

emp=Employee(12000,0.1)
print(emp.salaryafterincrement)
