def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if len(strs) == 0:
        return("")
    if len(strs)== 1:
        return(strs[0])
    prfi = strs[0]
    plen=len(prfi)
    for i in strs[1:]:
        while prfi != i[0:plen]:
            prfi=prfi[0:(plen-1)]
            plen-=1
            if plen==0:
                return("")
    return(prfi)
strs=["flower","flight","flow"]
result=longestCommonPrefix(strs)
print(f"the longest common prifix amonge {strs} is {result}".format(strs,result))
