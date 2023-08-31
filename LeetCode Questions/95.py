# 2057. Smallest Index With Equal Value

class Solution():
    def smallestEqual(self, nums):
        a=[]
        for i in range(len(nums)):
            if i%10==nums[i]:
                a.append(i)
        if len(a)==0:
            return -1
        return a[0]

a=Solution()
print(a.smallestEqual([0,1,2]))