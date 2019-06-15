class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 == str2:
            return str1
        if len(str1) >= len(str2):
            longer_str = str1
            shorter_str = str2
        else:
            longer_str = str2
            shorter_str = str1
        longest_slice = ""
        for i in range(1, int((len(longer_str) / 2))+1):
            str_slice = longer_str[:i]
            if len(longer_str) / i == len(longer_str) // i:
                m = len(longer_str) // i
                if len(shorter_str) / i == len(shorter_str) // i:
                    n = len(shorter_str) // i
                    if str_slice * m == longer_str and str_slice * n == shorter_str:
                        longest_slice = str_slice
        return longest_slice