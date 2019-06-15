class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        if s == '':
	        return -1
        for i in s:
	        d[i] = 1 if i not in d else d[i]+1
        for index, item in enumerate(s):
            if d[item] == 1:
                return index
        return -1
