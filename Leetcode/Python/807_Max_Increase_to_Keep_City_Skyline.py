class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row_skyline = list(map(max, grid))
        column_skyline = list(map(max, *grid))
        return sum(min(rm, cm) for rm in row_skyline for cm in column_skyline) - sum(map(sum, grid))
