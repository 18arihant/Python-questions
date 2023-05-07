# 2011 Final Value of Variable After Performing Operations

class Sol:
    def ans(self,operator):
        x=0
        for i in range(len(operator)):
            if  operator[i]=='++x':
                x=x+1
            elif operator[i]=='x++':
                x=x+1
            elif operator[i]=='x--':
                x=x-1
            elif operator[i]=='--x':
                x=x-1

        return x

b=Sol()
print(b.ans(['x++','x--'])) 