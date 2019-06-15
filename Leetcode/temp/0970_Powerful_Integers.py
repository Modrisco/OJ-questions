class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        from math import log
        if bound == 0:
            return []
        if x == 1:
            log_x = 1
        else:
            log_x = int(log(bound, x))
        if y == 1:
            log_y = 1
        else:
            log_y = int(log(bound, y))
        result = set()
        for i in range(log_x+1):
            for j in range(log_y+1):
                square_sum = x ** i + y ** j
                if square_sum <= bound:
                    result.add(square_sum)
        return sorted(list(result))
