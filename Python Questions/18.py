# recursive function to calculate sum of first 10 natural numbers

def sum_n(n):
    if n==1:
        return 1
    return sum_n(n-1) + n 

b= int(input("Enter a number:"))
a=sum_n(b)
print(a)
