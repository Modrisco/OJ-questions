class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # space is not O(1)...
        if not s.strip():
            return ''
        s = s.split(' ')
        res = []
        for i in s:
            if not i.strip():
                continue
            res.append(i)
        return ' '.join(res[::-1])
        # one line but space is not O(1)
        # return ' '.join(s.split()[::-1])
        
