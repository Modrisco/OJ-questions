from copy import deepcopy
class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums_copy = deepcopy(nums)
        for i in range(len(nums)):
            nums[i] = nums_copy[(i-k) % len(nums)]
