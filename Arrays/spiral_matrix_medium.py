"""
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        left, right = 0, len(matrix[0]) - 1
        top, bottom = 0, len(matrix) - 1
        result = []
        if not matrix:
            return result
        while top <= bottom and left <= right:
            
            # Traverse the matrix from left to right along top row
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1

            # Traverse the matrix from top to bottom along right column
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1

            # Traverse the matrix from right to left along bottom row
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1
        return result