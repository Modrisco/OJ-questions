class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        # use two pointers to ensure no more smaller numbers after an increase
        # and no more larger numbers after a decrease
        low = 0
        high = len(S)
        result = []
        for i, x in enumerate(S):
            if x == 'I':
                result.append(low)
                low += 1
            else:
                result.append(high)
                high -= 1
        result.append(low)
        return result

