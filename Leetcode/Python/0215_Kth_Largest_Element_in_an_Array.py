class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return 0
        left = 0
        right = len(nums) - 1
        while left < right:
            l = left
            r = right
            pivot = nums[l]
            while l < r:
                while pivot >= nums[r] and l < r:
                    r -= 1
                nums[l] = nums[r]
                while pivot <= nums[l] and l < r:
                    l += 1
                nums[r] = nums[l]
            nums[l] = pivot
            
            if l == k-1:
                return nums[l]
            elif l < k-1:
                left = l + 1
            else:
                right = r - 1
        return nums[left]
