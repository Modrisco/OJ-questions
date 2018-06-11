class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == [] or matrix[0] * 0 == 0:
            return matrix
        m = len(matrix)
        n = len(matrix[0])
        elements = m * n
        pointer_x = 0
        pointer_y = 0
        left_edge = 0
        right_edge = n - 1
        top_edge = 0
        bottom_edge = m - 1
        output = []
        direction = 1
    
        while elements > 0:
            output.append(matrix[pointer_x][pointer_y])
            # from left to right
            if direction == 1:
                if pointer_y == right_edge:
                    direction = 2
                    top_edge += 1
                    pointer_x += 1
                else:
                    pointer_y += 1
            # from top to bottom
            elif direction == 2:
                if pointer_x == bottom_edge:
                    direction = 3
                    right_edge -= 1
                    pointer_y -= 1
                else:
                    pointer_x += 1
            # from right to left
            elif direction == 3:
                if pointer_y == left_edge:
                    direction = 4
                    bottom_edge -= 1
                    pointer_x -= 1
                else:
                    pointer_y -= 1
            # from bottom to top
            elif direction == 4:
                if pointer_x == top_edge:
                    direction = 1
                    left_edge += 1
                    pointer_y += 1
                else:
                    pointer_x -= 1
            elements -= 1
        return output
        
