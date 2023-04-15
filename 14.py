a=int(input("Enter number of rows to which you want star patters:"))
for i in range(a,-1,-1):
    for j in range(i-1,-1,-1):
        print("*" ,end=' ')
    print("\n")