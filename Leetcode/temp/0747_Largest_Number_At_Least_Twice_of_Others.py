from copy import deepcopy
class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_1 = sorted(list(set(deepcopy(nums))), reverse = True)
        if nums_1 == [1] or nums_1 == [0]:
            return 0
        elif len(nums_1) == 1:
            return -1
        elif nums_1[0] >= 2 * nums_1[1]:
            return nums.index(nums_1[0])
        return -1
        
        
