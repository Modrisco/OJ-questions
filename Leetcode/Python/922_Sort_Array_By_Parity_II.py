class Solution:
    def sortArrayByParityII(self, A: 'List[int]') -> 'List[int]':
        even = []
        odd = []
        result = []
        for i in range(len(A)):
            if A[i] % 2 == 0:
                even.append(A[i])
            else:
                odd.append(A[i])
        for i in range(len(even)):
            result.append(even[i])
            result.append(odd[i])
        return result
