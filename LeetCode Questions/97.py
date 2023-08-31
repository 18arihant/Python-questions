# 2149. Rearrange Array Elements by Sign

class Solution():
    def rearrangeArray(self, nums):
        positive = []
        negative = []
        
        for num in nums:
            if num > 0:
                positive.append(num)
            else:
                negative.append(num)
                
        result = [None] * len(nums)
        result[::2] = positive
        result[1::2] = negative
        
        return result
    
a=Solution()
print(a.rearrangeArray([3,1,-2,-5,2,-4]))