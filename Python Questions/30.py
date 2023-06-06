# sum of first n natural numbers

def num(n):
    s=0
    for i in range(1,n+1):
        s=s+i
    return s

a=int(input("Enter a number to which you want sum: "))
print(num(a))