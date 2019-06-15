class Solution:
    def sortArrayByParity(self, A: 'List[int]') -> 'List[int]':
        result = []
        for i in range(len(A)):
            if A[i] % 2 == 0:
                result = [A[i]] + result
            else:
                result += [A[i]]
        return result
