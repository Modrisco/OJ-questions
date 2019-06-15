class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        bin_list = list(bin(num)[2:])
        for i in range(len(bin_list)):
            bin_list[i] = '1' if bin_list[i] == '0' else '0'
        return int(''.join(bin_list), 2)
