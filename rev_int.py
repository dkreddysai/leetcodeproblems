def reverse(x):
        """
        :type x: int
        :rtype: int
        """
        revers=0
        n=x
        
        if x<0:
            x=0-x
        while x!=0:
            revers=(revers*10)+(x%10)
            x=x//10
        if revers < 2**31 and revers>(-2)**31:
            if n<0:
                return -revers
            else:
                return revers
        else:
            return 0
m=reverse(-876)
print(m)
