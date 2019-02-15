class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        result = []
        even_sum = sum(x for x in A if x % 2 == 0)
        for i in range(len(A)):
            ori_num = A[queries[i][1]]
            A[queries[i][1]] += queries[i][0]
            if A[queries[i][1]] % 2 != 0 and ori_num % 2 == 0:
                even_sum -= ori_num
            if A[queries[i][1]] % 2 == 0:
                if ori_num % 2 == 0:
                    even_sum -= ori_num
                    even_sum += A[queries[i][1]]
                else:
                    even_sum += A[queries[i][1]]
            result.append(even_sum)
        return result
