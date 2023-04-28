# to print table of any number in reverse order
n= int(input('Enter a number of which you want the table:'))
for i in range(10,0,-1):
    print(n, "*", i, "=", (n*i) )
