class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        l = len(s)
        if l <= 1:
            return True
        x = 0
        y = l-1
        while x < y:
            if s[x] != s[y]:
                return False
            else:
                x += 1
                y -= 1
        return True
