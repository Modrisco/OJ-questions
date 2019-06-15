class Solution(object):
    def canThreePartsEqualSum_brute_force(self, A):
        """
        :type A: List[int]
        :rtype: bool
        two pointers but timeout......
        """
        for i, x in enumerate(A):
            for j, x in enumerate(A):
                if sum(A[:i]) == sum(A[i:j]) == sum(A[j:]):
                    return True
        return False

    def canThreePartsEqualSum(self, A):
        """
        :type A: List[int]
        :rtype: bool
        if the answer is true, sum A must be divided by 3
        find the first part and find the other two
        """
        if sum(A) % 3 != 0:
            return False
        partition = int(sum(A) / 3)
        found = False
        c = 0
        for num in A:
            c += num
            if c == partition * 2 and found:
                return True
            if c == partition:
                found = True
        return False
