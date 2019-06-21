class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        m = 0
        i = 1
        if n == 0:
            return True
        if len(flowerbed) <= 2:
            if n == 2:
                return False
            return True if sum(flowerbed) < 1 else False
        for i in range(len(flowerbed)):
            if i == 0:
                if flowerbed[i+1] == 0 and flowerbed[i] == 0:
                    m += 1
                    flowerbed[i] = 1
            elif 0 < i < len(flowerbed) - 1:
                if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                    m += 1
                    flowerbed[i] = 1
            else:
                if flowerbed[i-1] == 0 and flowerbed[i] == 0:
                    m += 1
                    flowerbed[i] = 1
        return True if m >= n else False
