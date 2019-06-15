class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for index, value in enumerate(numbers):
            dict[value] = index
        for index, value in enumerate(numbers):
            if target - value in dict and dict[target - value] != index:
                return [index + 1, dict[target - value] + 1]
