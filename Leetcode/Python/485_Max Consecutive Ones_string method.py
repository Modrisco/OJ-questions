class Solution
    def findMaxConsecutiveOnes(self, nums)
        '''
        type nums List[int]
        rtype int
        '''
        # nums = [1,1,0,1,1,1]
        s = ''.join(str(i) for i in nums)
        # s = '110111', split s by '0', s = ['11', '111']
        return len(max(s.split('0')))
