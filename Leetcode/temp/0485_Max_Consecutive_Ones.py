class Solution:
    def findMaxConsecutiveOnes_string(self, nums):
        '''
        type nums List[int]
        rtype int
        '''
        # nums = [1,1,0,1,1,1]
        s = ''.join(str(i) for i in nums)
        # s = '110111', split s by '0', s = ['11', '111']
        return len(max(s.split('0')))

    def findMaxConsecutiveOnes_pointer(self, nums):
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


