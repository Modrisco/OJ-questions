class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        from collections import Counter
        if len(deck) <= 1:
            return False
        def gcd(x, y):
            if y == 0:
                return x
            else:
                return gcd(y, x%y)
        counter = Counter(deck).values()
        res = counter[0]
        for c in counter[1:]:
            res = gcd(res, c)
        return True if res != 1 else False

