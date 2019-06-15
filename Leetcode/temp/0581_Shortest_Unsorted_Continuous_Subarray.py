class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        smallest = nums[0]
        largest = nums[-1]
        left = 0
        right = 0
        # the most chaos, the whole list need to be changed
        if smallest != min(nums) and largest != max(nums):
            return len(nums)
        if smallest != min(nums):
            return nums.index(min(nums)) + 1
        if largest != max(nums):
            return len(nums) - nums.index(max(nums))
        if nums == sorted(nums):
            return 0
        for i, x in enumerate(nums):
            if x < smallest:
                left = i - 1
                break
            smallest = x
        nums = nums[::-1]
        for i, x in enumerate(nums):
            if x > largest:
                right = len(nums) - i
                break
            largest = x
        return right - left + 1
