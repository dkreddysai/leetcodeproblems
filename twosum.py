#https://leetcode.com/problems/two-sum/submissions/
#Two Sum
class Solution:
    def twoSum(nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if target - nums[i] == nums[j]:
                    return([i,j])
        return None            
            
    test=[2,7,11,15]
    target=18
    print(twoSum(test,target))    
