class Solution(object):
    def isAlienSorted_naive(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        word_map = dict()
        word_list = []
        for i in range(len(order)):
            word_map[i] = order[i]
        for word in words:
            letter_to_num = []
            for l in word:
                letter_to_num.append(list(word_map.keys())[list(word_map.values()).index(l)])
            word_list.append(letter_to_num)
        if word_list == sorted(word_list):
            return True
        else:
            return False

    def isAlienSorted_ans(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        letter_map = {c: i for i, c in enumerate(order)}

        for i in range(len(words) - 1):
            word_1 = words[i]
            word_2 = words[i + 1]
            # Find the first difference word1[k] != word2[k].
            for j in range(min(len(word_1), len(word_2))):
                if word_1[j] != word_2[j]:
                    if letter_map[word_1[j]] > letter_map[word_2[j]]:
                        return False
                    break
                else:
                    # ['apple', 'app'] -> False
                    if len(word_1) > len(word_2):
                        return False
        return True
