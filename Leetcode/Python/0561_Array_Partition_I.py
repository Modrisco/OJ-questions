class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # return sum of odd items in the sorted list...
        return sum(sorted(nums)[::2])
