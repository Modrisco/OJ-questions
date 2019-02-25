class Solution(object):
    def reverseOnlyLetters_stack(self, S):
        """
        :type S: str
        :rtype: str
        """
        letters = []
        list_S = list(S)
        for i in range(len(list_S)):
            if 65 <= ord(list_S[i]) <= 90 or 97 <= ord(list_S[i]) <= 122:
                letters.append(list_S[i])
                list_S[i] = '~'
        for i in range(len(list_S)):
            list_S[i] = letters.pop() if list_S[i] == '~' else list_S[i]
        return ''.join(list_S)

    def reverseOnlyLetters_pointer(self, S):
        """
        :type S: str
        :rtype: str
        """
        result = []
        end = len(result) - 1
        for i, x in enumerate(S):
            if x.isalpha():
                while not S[end].isalpha():
                    end -= 1
                result.append(S[end])
                end -= 1
            else:
                result.append(x)
        return ''.join(result)
