class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        return list(map(int, str(int(''.join(list(map(str, A)))) + K)))
