class Solution(object):
    def twoCitySchedCost_greedy(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        distance = 0
        person = len(costs)
        gap_list = sorted(costs, key=lambda x: x[0]-x[1])
        for i in range(person):
            distance += gap_list[i][0] if i < person/2 else gap_list[i][1]
        return distance