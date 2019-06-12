class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        return str(int(num1) + int(num2))
    
    def addStrings_normal(self, num1: str, num2: str) -> str:
        nt = {
            '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
            '6': 6, '7': 7, '8': 8, '9': 9
        }
        
        i = len(num1) - 1
        j = len(num2) - 1
        carry = 0
        res = ''

        while i >= 0 or j >= 0:
            n1 = nt[num1[i]] if i >= 0 else 0
            n2 = nt[num2[j]] if j >= 0 else 0
            n = n1 + n2 + carry
            
            if n >= 10:
                carry = 1
                n -= 10
            else:
                carry = 0

            res = str(n) + res

            i -= 1
            j -= 1
            
        if carry == 1:
            res = "1" + res

        return res