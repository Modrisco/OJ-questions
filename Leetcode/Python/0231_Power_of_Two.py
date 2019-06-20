class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # n ** 2 & n ** 2 - 1 = 0
        # e.g: 8 -> 1000 & 7 -> 0111 = 0
        return True if n > 0 and n & (n - 1) == 0 else False
