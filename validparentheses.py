def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    close_map={"(":")","{":"}","[":"]"}
    opens=[]
    for symbol in s:
        if symbol in close_map.keys():
            opens.append(symbol)
        elif opens==[] or symbol != close_map[opens.pop()]:
            return False
    return opens==[]
if __name__=="__main__":
    s=input("enter a string of parentheses")
    
    result=isValid(s)
    if result:
        print("valid parentheses")
    else:
        print("not a valid parentheses")
