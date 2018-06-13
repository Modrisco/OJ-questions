class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []
        s = s.split()
        for e in s:
            res.append(e)
        for i in range(len(res)):
            res[i] = res[i][::-1]
        return ' '.join(e for e in res)
