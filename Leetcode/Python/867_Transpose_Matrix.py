class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        flipped_matrix = []
        for i in range(len(A[0])):
            line = []
            for j in range(len(A)):
                line.append(A[j][i])
            flipped_matrix.append(line)
        return flipped_matrix
