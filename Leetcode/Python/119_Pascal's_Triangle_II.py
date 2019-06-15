class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        tri = [1] * (rowIndex+1)
        for i in range(2, rowIndex+1):
            for j in range(1, i):
                tri[i-j] += tri[i-j-1]
        return tri
        
