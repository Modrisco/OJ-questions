class Solution:
    def convertToTitle(self, n: int) -> str:
        import string
        letters = list(string.ascii_uppercase)
        result = []
        if n == 0:
            return ""
        while n > 0:
            result.append(letters[(n-1) % 26])
            n = (n - 1) // 26
        return ''.join(result[::-1])

