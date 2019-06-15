class Solution(object):
    def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """
        words = text.split()
        third = []
        for i in range(0, len(words)-2):
            if words[i] == first and words[i+1] == second:
                third.append(words[i+2])
        return third
