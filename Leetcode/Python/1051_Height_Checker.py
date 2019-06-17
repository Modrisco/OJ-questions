class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_height = sorted(heights)
        wrong = 0
        for i, x in enumerate(heights):
            if x != sorted_height[i]:
                wrong += 1
        return wrong
