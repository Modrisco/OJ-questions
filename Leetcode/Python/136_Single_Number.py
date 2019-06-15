class Solution:
    def singleNumber_hash(self, nums: 'List[int]') -> 'int':
        from collections import defaultdict
        if len(nums) == 1:
            return nums[0]
        d = defaultdict(int)
        for i in nums:
            d[i] += 1
        for i in d:
            if d.get(i) == 1:
                return i

    def singleNumber_xor(self, nums: 'List[int]') -> 'int':
        for i in range(1, len(nums)):
            nums[0] ^= nums[i]
        return nums[0]

    def singleNumber_math(self, nums):
        return 2 * sum(set(nums)) - sum(nums)
