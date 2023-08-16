#https://leetcode.com/problems/happy-number/submissions/
#Happy Number
def sqrSum(n):
    tot =  0
    while n > 0:
        tot += pow(n % 10, 2)
        n //= 10
    return tot

num = int(input('Enter Any Value = '))
temp = num

while temp != 1 and temp != 4:
    temp = sqrSum(temp)

if temp == 1:
    print('It is a Happy Number')
else:
    print('It is Not')
