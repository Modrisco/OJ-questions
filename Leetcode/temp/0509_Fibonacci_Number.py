class Solution(object):
    def fib_formula(self, N):
        """
        :type N: int
        :rtype: int
        """
        from math import sqrt
        return int(((1+sqrt(5))**N - (1-sqrt(5))**N)/(2**N*sqrt(5)))


    def fib_recursive(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 0:
            return 0
        elif N == 1:
            return 1
        else:
            return self.fib(N - 1) + self.fib(N - 2)

    def fib_add(self, N):
        a, b = 0, 1
        for _ in range(N):
            a, b = b, a + b
        return a

