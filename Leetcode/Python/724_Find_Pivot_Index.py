class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_sum = sum(nums)
        current_sum = 0
        for i in range(len(nums)):
            if current_sum * 2 + nums[i] == total_sum:
                return i
            current_sum += nums[i]
        return -1
