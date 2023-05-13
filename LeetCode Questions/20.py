# 1662. Check If Two String Arrays are Equivalent

class Solution:
    def join(self,word1,word2):
        a="".join(word1)
        b="".join(word2)
        print(a,b)
        if a==b:
            return True
        else:
            return False
a=Solution()
print(a.join(["ab", "c"],["a", "bc"]))
    
