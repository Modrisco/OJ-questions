class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        left_pointer = 0
        right_pointer = 0
        current_sum = 0
        minimum = len(nums)
        if sum(nums) < s:
            return 0
        # set double pointers and make right pointer move
        # when current sum >= s, move left pointer
        # move pointer and current sum minus the older item of left pointer
        # check if the current is still larger than s
        for right_pointer in range(len(nums)):
            current_sum += nums[right_pointer]
            while current_sum >= s and left_pointer <= right_pointer:
                minimum = min(minimum, right_pointer - left_pointer + 1)
                current_sum -= nums[left_pointer]
                left_pointer += 1
        return minimum
        
