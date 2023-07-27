#https://leetcode.com/problems/climbing-stairs/description/
#Climbing Stairs
class Solution(object):
    def climbStairs(n):
        """
        :type n: int
        :rtype: int
        """
        def dp(n, cache):
            if n not in cache:
                cache[n] = dp(n-1, cache) + dp(n-2, cache)
            return cache[n]
        return dp(n, {1: 1, 2: 2})
    n=3
    print(climbStairs(n))
