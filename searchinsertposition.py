class Solution():
    def searchInsert(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        try:
            for i, num in enumerate(nums):
                if target == num or target < num:
                    return i
            return i + 1
        except:
            return 0
    nums = [1, 3, 5, 6]
    n = len(nums)
    target = 7
    print(searchInsert(nums,target))
