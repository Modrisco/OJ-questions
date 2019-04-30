class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        if len(A) == len(B) == 0:
            return True
        for i in range(len(A)):
            C = A[i:] + A[:i]
            if C == B:
                return True
        return False
