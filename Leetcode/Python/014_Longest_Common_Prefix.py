class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        # strs = ['ab', 'aa', 'bb']
        # list(zip(*strs)) = [('a','a','b'),('b','a','b')]
        # learn how to use zip and *virable
        letters = list(zip(*strs))
        for i in range(len(letters)):
            if len(set(letters[i])) != 1:
                return strs[0][:i]
        return min(strs)
