# 2574 Left and Right Sum Differences

class Solution:
    def sum(self,nums):
        if len(nums)>1:
            leftsum=[0]
        else:
        rightsum=[0]
        answer=[]
        left=0
        right=0
        for i in range(0,len(nums)-1):
            left+=nums[i]
            leftsum.append(left)
        # print(leftsum)
        for i in range(len(nums)-1,-1,-1):
            right+=nums[i]
            rightsum.insert(0,right)
            if len(rightsum)==len(nums):
               break
        # print(rightsum)
        for i in range(len(nums)):
            if leftsum[i]>rightsum[i]:
                answer.append((leftsum[i]-rightsum[i]))
            else:
                answer.append((rightsum[i]-leftsum[i]))
        return answer

a=Solution()
print(a.sum([10,4,8,3]))

            


        
