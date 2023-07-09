def removeElement(nums,val):
    """
    :type nums: List[int]
    :rtype: int
    """
    k=0
    for i in range(len(nums)):
        if nums[i]!=val:
            nums[k]=nums[i]
            k+=1
    return k
if __name__=="__main__":
    val=1
    nums=[0,1,1,1,2,3,4,5,6,6,6,6,7,8]
    result=removeElement(nums,val)
    print(f"after removing {val} list is {nums}".format(val,result))
