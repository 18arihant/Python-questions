# 2506. Count Pairs Of Similar Strings

class Solution():
    def similarPairs(self, words):
        c=0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if set(words[i])==set(words[j]):
                    c+=1
        return c

a=Solution()
print(a.similarPairs(["aba","aabb","abcd","bac","aabc"]))