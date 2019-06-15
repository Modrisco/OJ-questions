class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        from collections import Counter
        record = Counter(s)
        if record['A'] > 1 or 'LLL' in s:
            return False
        return True
