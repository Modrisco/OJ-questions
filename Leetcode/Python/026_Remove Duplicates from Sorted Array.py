class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        pointer = 0
        # replace item on pointer with new item
        for num in nums:
            if num > nums[pointer]:
                pointer += 1
                nums[pointer] = num
        return pointer + 1
