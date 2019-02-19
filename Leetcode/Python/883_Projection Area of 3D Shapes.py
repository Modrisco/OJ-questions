class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        top, front, side = 0, 0, 0
        for i in range(len(grid)):
            front += max(grid[i])
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    top += 1
        flipped_grid = list(map(list, zip(*grid)))
        for i in range(len(flipped_grid)):
            side += max(flipped_grid[i])
        return top + front + side
