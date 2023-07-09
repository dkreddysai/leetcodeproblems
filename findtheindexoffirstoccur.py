def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    if needle=="":
        return 0
    for i in range(len(haystack)+1-len(needle)):
        if haystack[i:i+len(needle)]==needle:
            return i
    return -1
if __name__=="__main__":
    
    haystack="leetcode"
    needle="code"
    result=strStr(haystack, needle)
    print(f"index of first occurrence of  {needle} in {haystack} is {result}".format(needle,haystack,result))  
