class Solution:
    def majorityElement_hash(self, nums: 'List[int]') -> 'int':
        from collections import defaultdict
        d = defaultdict(int)
        for i in nums:
            d[i] += 1
        return max(d.keys(), key=d.get)

    def majorityElement_list(self, nums: 'List[int]') -> 'int':
        return sorted(nums)[len(nums) // 2]
