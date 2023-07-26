class Solution(object):
    def plusOne(digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits=str(int(''.join([str(x) for x in digits]))+1)
        ret=[]
        for i in range(len(digits)):
            ret.append(int(digits[i:i+1]))
        return ret
    digits=[4,3,2,1]
    print(plusOne(digits))
