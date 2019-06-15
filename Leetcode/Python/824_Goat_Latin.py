class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        vowel = {'a', 'e', 'i', 'o', 'u'}
        words = S.split(' ')
        for i,x in enumerate(words):
            suffix = 'm' + (i+2) * 'a'
            if x[0].lower() not in vowel:
                word = list(x)
                fixed_word = word[1:]
                fixed_word.append(word[0])
                words[i] = ''.join(fixed_word)
            words[i] += suffix
        return ' '.join(words)
