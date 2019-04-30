class Solution:
    def baseNeg2(self, N: int) -> str:
        if N == 0:
            return '0'
        result = ''
        while N:
            remainder = N % (-2)
            N = -(N >> 1)
            result += str(abs(remainder))
        return result[::-1]
