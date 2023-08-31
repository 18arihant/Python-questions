# 2108. Find First Palindromic String in the Array

class Solution():
    def firstPalindrome(self, words):
        a=""
        for i in words:
            if i==i[::-1]:
                a=i
                break
        return a

a=Solution()
print(a.firstPalindrome(["abc","car","ada","racecar","cool"]))