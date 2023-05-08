# 2574 Left and Right Sum Differences

class Solution:
    def sum(self,nums):
        leftsum=[0]
        rightsum=[]
        answer=[]
        left=0
        right=0
        for i in range(0,len(nums)-1):
            left+=nums[i]
            leftsum.append(left)
        print(leftsum)
        # for i in range(len(nums)):
        #     if nums[-i]==(len(nums)+1):
        #         right=0
        #         rightsum.append(right)
        #     else:
        #         right+=nums[-i]
        #         rightsum.append(right)
        # for i in range(len(nums)):
        #     if leftsum[i]>rightsum[i]:
        #         answer.append((leftsum[i]-rightsum[i]))
        #     else:
        #         answer.append((rightsum[i]-leftsum[i]))
        # return answer

a=Solution()
print(a.sum([10,4,8,3]))

            


        
