class Solution(object):
    def allCellsDistOrder(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        coordinates = []
        for i in range(R):
            for j in range(C):
                coordinates.append([i, j])
        coordinates = sorted(coordinates, key=lambda x: abs(x[0] - r0) + abs(x[1] - c0))
        return coordinates
