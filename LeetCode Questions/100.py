# 1436. Destination City

class Solution():
    def destCity(self, paths):
        source = set()
        dest = set()
        for l in paths:
            source.add(l[0])
            dest.add(l[1])
        return list(dest - source)[0]

a=Solution()
print(a.destCity([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))