class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        result = []
        for num in range(left, right + 1):
            if self.is_self_dividing(num) is True:
                result.append(num)
        return result

    def is_self_dividing(self, num):
        digits = set()
        ori_num = num
        while num > 0:
            if num % 10 == 0:
                return False
            digits.add(num % 10)
            num //= 10
        for n in digits:
            if ori_num % n != 0:
                return False
        return True
