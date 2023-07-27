#https://leetcode.com/problems/sqrtx/
#Sqrt(x)
class Solution():
    def mySqrt(x):
        """
        :type x: int
        :rtype: int
        """
        l = 1
        r = x + 1
        while l < r:
            m = (l + r) // 2
            if m * m > x:
                r = m
            else:
                l = m + 1
        return l - 1
    x=8
    print(mySqrt(x))
