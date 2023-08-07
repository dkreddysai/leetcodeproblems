#https://leetcode.com/problems/divide-two-integers/submissions/
#Divide Two Integers
class Solution():
    def divide(dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend*divisor>0:
            res=abs(dividend)//abs(divisor)
        else:
            res=-(abs(dividend)//abs(divisor))
        intmin=-(2**31)
        intmax=(2**31)-1
        return res if intmin<=res<=intmax else intmax
    if __name__ == '__main__':
        d = divide(18,3)
        print(d)
    
