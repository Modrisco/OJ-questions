class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        j = dict.fromkeys(list(J), 0)
        for e in S:
            if e in j:
                j[e] += 1
        return sum(j.values())
