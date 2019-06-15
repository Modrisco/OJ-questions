class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # Convert string into an integer, plus one. Finally, convert the integer back to string and return a list
        return list(map(int, str(int(''.join(map(str, digits))) + 1)))
