class Solution(object):
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        if len(A) <= 1:
            return 0
        gap = max(A) - min(A)
        if gap < 2 * K:
            return 0
        return gap - 2 * K
