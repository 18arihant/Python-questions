#star patter
# * * *
# * *
# *
a=int(input("Enter number of rows to which you want star patters:"))

for i in range(a,0,-1):
    for j in range(0,i):
        print("*" , end=' ')
    print("\n")
    