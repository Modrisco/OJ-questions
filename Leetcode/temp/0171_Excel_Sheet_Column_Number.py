class Solution:
    def titleToNumber_slow(self, s: str) -> int:
        import string
        letters = list(string.ascii_uppercase)
        s_list = list(s)
        result = 0
        for i, e in enumerate(s_list):
            result += (letters.index(e) + 1) * (26 ** (len(s_list) - i - 1))
        return result
        
    
    def titleToNumber_fast(self, s: str) -> int:
        dict = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
        result = 0
        n = 0
        for i in range(len(s)-1,-1,-1):
            result += dict[s[i]]*(26**n)
            n += 1
            
        return result
