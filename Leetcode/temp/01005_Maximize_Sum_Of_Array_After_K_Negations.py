class Solution(object):
    def largestSumAfterKNegations(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        sorted_A = sorted(A)
        for i, x in enumerate(sorted_A):
            if x < 0 < K:
                sorted_A[i] = -x
                K -= 1
        sorted_A = sorted(sorted_A)
        if K % 2 != 0:
            sorted_A[0] = -sorted_A[0]
        return sum(sorted_A)
