class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row_1 = {'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'}
        row_2 = {'a', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 's'}
        row_3 = {'b', 'c', 'm', 'n', 'v', 'x', 'z'}
        result = []
        for word in words:
            word_set = set(list(word.lower()))
            if word_set.issubset(row_1) or word_set.issubset(row_2) or word_set.issubset(row_3):
                result.append(word)
        return result
