class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum = 0
        current = 0
        for i in nums:
            if i == 1:
                current += 1
                if current > maximum:
                    maximum = current
            else:
                current = 0
        return maximum
        
