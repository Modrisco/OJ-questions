class Solution(object):
    def bitwiseComplement(self, N):
        """
        :type N: int
        :rtype: int
        """
        binary = list(bin(N))
        for i in range(2, len(binary)):
            binary[i] = '0' if binary[i] == '1' else '1'
        return int(''.join(binary), 2)

    def bitwiseComplementMath(self, N):
        digit, num = 1, N
        while N > 1:
            digit += 1
            N = N//2
        return 2**digit - 1 - num
