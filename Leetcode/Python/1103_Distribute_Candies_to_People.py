class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        if candies == 0 or num_people == 0:
            return
        res = [0] * num_people
        n = 1
        while candies >= 0:
            if candies >= n:
                res[(n-1) % num_people] += n 
            else:
                res[(n-1) % num_people] += candies
            candies -= n
            n += 1
        return res
