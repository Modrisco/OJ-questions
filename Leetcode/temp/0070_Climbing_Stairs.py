# Dynamic Programming
# Fibonacci list...


class Solution(object):
    def climbStairs(self, n):
        if n <= 1:
            return 1
        else:
            l = [1] * (n+1)
            for i in range(2, n+1):
                l[i] = l[i-1] + l[i-2]
        return l[-1]
