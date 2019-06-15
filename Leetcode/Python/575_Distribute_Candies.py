class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        kinds = len(set(candies))
        return kinds if kinds < (len(candies) / 2) else int(len(candies) / 2)
