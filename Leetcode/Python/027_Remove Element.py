class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # double pointer from left to right and from right to left
        # a pointer move when the item does not equal to val
        head = 0
        tail = len(nums) - 1
        pointer = 0
        while head <= tail:
            if nums[head] == val:
                head += 1
            elif nums[tail] == val:
                tail -= 1
            else:
                nums[pointer] = nums[head]
                head += 1
                pointer += 1
        return pointer
        
