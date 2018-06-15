class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        # double pointers, head and tail
        head = 0
        tail = len(nums) - 1
        while head < tail:
            # pop the first item which is 0, and append a
            # new 0 to the end
            if nums[head] == 0:
                nums.pop(head)
                nums.append(0)
                tail -= 1
            else:
                head += 1
