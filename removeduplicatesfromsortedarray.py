def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums)==0:
        return 0
    j=0
    for i in range(1,len(nums)):
        if nums[i]!=nums[j]:
            j+=1
            nums[j]=nums[i]
    return j+1
nums=[1,1,1,1,2,2,3,3,4]
print(removeDuplicates(nums))
