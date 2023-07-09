s=input()
def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    dev=0
    for i in range(len(s)):
        if i+1 !=len(s) and d[s[i]]<d[s[i+1]]:
            dev=dev-d[s[i]]
        else:
            dev = dev +d[s[i]]
    return dev
print(romanToInt(s))
