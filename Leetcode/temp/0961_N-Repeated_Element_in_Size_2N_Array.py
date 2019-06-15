class Solution:
    def repeatedNTimes(self, A: 'List[int]') -> 'int':
        from collections import Counter
        dic = Counter(A)
        for i in A:
            if dic[i] > 1:
                return i
