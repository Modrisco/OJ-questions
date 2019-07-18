class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        orderBy = {x: i for i, x in enumerate(arr2)}
        return sorted(arr1, key=lambda i: orderBy.get(i, i + 1000))
