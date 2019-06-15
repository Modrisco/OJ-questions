class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if len(nums) * len(nums[0]) != r * c:
            return nums
        all_num = [item for sublist in nums for item in sublist]
        index = 0
        reshaped_matrix = []
        for i in range(r):
            row = []
            for j in range(c):
                row.append(all_num[index])
                index += 1
            reshaped_matrix.append(row)
        return reshaped_matrix
