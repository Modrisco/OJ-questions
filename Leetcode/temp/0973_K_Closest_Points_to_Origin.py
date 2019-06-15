class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        for p in points:
            p.append(p[0] ** 2 + p[1] ** 2)
        points = sorted(points, key=lambda p: p[2])
        points = [point[:2] for point in points]
        return points[:K]
