class Solution:
    def judgeCircle(self, moves: 'str') -> 'bool':
        from collections import Counter
        direction = Counter(moves)
        if direction['L'] != direction['R'] or direction['U'] != direction['D']:
            return False
        return True
