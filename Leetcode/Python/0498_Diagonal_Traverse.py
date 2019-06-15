class Solution:
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # easier than 498...
        if matrix == [] or matrix[0] * 0 == 0:
            return matrix
        m = len(matrix)
        n = len(matrix[0])
        top_edge = 0
        bottom_edge = m - 1
        left_edge = 0
        right_edge = n - 1
        output = []
        elements = m * n
        direction = 1
        pointer_x = 0
        pointer_y = 0
        while elements > 0:
            output.append(matrix[pointer_x][pointer_y])
            # from S-W to N-E
            if direction == 1:
                # touch the top edge, move right
                if pointer_x == top_edge and pointer_y != right_edge:
                    direction = 2
                    pointer_y += 1
                # touch the right edge, move down
                elif pointer_y == right_edge:
                    direction = 2
                    pointer_x += 1
                else:
                    pointer_x -= 1
                    pointer_y += 1
            # from N-E to S-W
            elif direction == 2:
                # touch the left edge, move down
                if pointer_x != bottom_edge and pointer_y == left_edge:
                    direction = 1
                    pointer_x += 1
                # touch the bottom edge, move right
                elif pointer_x == bottom_edge:
                    direction = 1
                    pointer_y += 1
                else:
                    pointer_x += 1
                    pointer_y -= 1
            elements -= 1
        return output
        
