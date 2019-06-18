class Solution(object):
    def duplicateZeros_naive(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        i = 0
        while i < len(arr) - 1:
            if arr[i] != 0:
                i += 1
            if arr[i] == 0:
                arr[i+2:] = arr[i+1:-1]
                if i < len(arr) - 1:
                    arr[i+1] = 0
                i += 2

    def duplicateZeros_better(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        i = 0
        n = len(arr)
        while i < n:
            if arr[i] == 0:
                # [1,2,0,4,5] --> [1,2,0,0,4,5]
                arr[i:i] = [0]
                del(arr[-1])
                i += 1
            i += 1