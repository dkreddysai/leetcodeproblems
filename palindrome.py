def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    temp=x
    result=False
    revers=0
    if x<0:
        return result
    else:
        while temp > 0:
            revers=revers*10+temp%10;
            temp=temp//10

        if revers == x:
            result=True
        return result
if __name__=="__main__":
    
    str=int(input("enter a number"))
    result=isPalindrome(str)
    if result:
        print(f"{str} is a palindrom".format(str))
    else:
        print(f"{str} is not a palindrom".format(str))
