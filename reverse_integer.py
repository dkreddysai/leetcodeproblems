#https://leetcode.com/problems/reverse-integer/
#Reverse Integer   
def recur_reverse(num):  
    global revr_num   
    if (num > 0):  
        Reminder = num % 10  
        revr_num = (revr_num * 10) + Reminder  
        recur_reverse(num // 10)  
    return revr_num
num = 123  
revr_num = 0  
revr_num = recur_reverse(num)  
print(revr_num)  
