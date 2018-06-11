class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        # nums = [2,7,9,11]
        for index, value in enumerate(nums):
            dict[value] = index
            # dict = {2:0, 7:1, 9:2, 11:3}
        for index, value in enumerate(nums):
            if target - value in dict and dict[target - value] != index:
                return (index, dict[target - value])
        
