#to print the multiplication table of a given number
a=int(input("Enter a number of which you want a table:"))
for i in range(1,11):
    print(a, "x", i, '=',(i*a) )