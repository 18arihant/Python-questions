
class find:
    def reverse(self, x):
        a=str(x)
        b=list(a)
        b.reverse()
        d="".join(b)
        print(a)
        print(b)
        return int(d)
    
a=find()
print(a.reverse(243))
