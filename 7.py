#to detect double spaces and replace it with single space
a=input("Enter a line:")
c= a.find("  ")
print("The double spaces is found at index:",c)
d= a.replace("  "," ")
print("The replaced string:",d)