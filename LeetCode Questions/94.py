# 2460. Apply Operations to an Array

class Solution():
    def applyOperations(self, nums):
        for i in range(len(nums)):
            if i<=len(nums)-2:
                if nums[i] == nums[i + 1]:
                    nums[i]=nums[i]*2
                    nums[i+1]=0
            
        for i in nums:
            if i==0:
                nums.remove(i)
                nums.append(i)
        return nums

a=Solution()
print(a.applyOperations([1,2,2,1,1,0]))