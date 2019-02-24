class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        people = dict()
        for i in range(1, N+1):
            people[i] = {}
            people[i]['trusts'] = 0
            people[i]['trusted'] = 0
        for i,x in enumerate(trust):
            people[x[0]]['trusts'] += 1
            people[x[1]]['trusted'] += 1
        for p in people:
            if people[p]['trusts'] == 0 and people[p]['trusted'] == N-1:
                return p
        return -1
