class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        res = [0] * len(T)
        for i in range(len(T)):
            while len(stack) != 0 and T[stack[-1]] < T[i]:
                ori = stack.pop()
                res[ori] = i - ori
            stack.append(i)
        return res

