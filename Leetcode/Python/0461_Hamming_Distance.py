class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        bin_x = bin(x)[2:]
        bin_y = bin(y)[2:]
        diff = abs(len(bin_x) - len(bin_y))
        if len(bin_x) < len(bin_y):
            bin_x = '0' * diff + bin_x
        else:
            bin_y = '0' * diff + bin_y
        dis = 0
        for i in range(len(bin_x)):
            if bin_x[i] != bin_y[i]:
                dis += 1
        return dis
