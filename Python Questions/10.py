# to greet all person names start with s
a=int(input("How many names do you want to store in a list:"))
b=[]
for i in range(1,a+1):
    l=input("Enter a name:")
    b.append(l)
print(b)
for i in b:
     if (i[0]=="s" or i[0]=="S"):
        print("hello "+ i)
