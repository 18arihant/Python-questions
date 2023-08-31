# 2828. Check if a String Is an Acronym of Words

class Solution():
    def isAcronym(self, words, s):
        ans=""
        for word in words:
            ans+=word[0]

        return ans==s  

a=Solution()
print(a.isAcronym(["an","apple"],'a'))