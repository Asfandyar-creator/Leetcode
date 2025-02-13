"""
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104

"""

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:  # Edge case: empty matrix
            return False
        
        m, n = len(matrix), len(matrix[0])  # Dimensions
        low, high = 0, (m * n) - 1  # Virtual array indices

        while low <= high:
            mid = low + (high - low) // 2
            row, col = mid // n, mid % n  # Convert mid to 2D index
            num = matrix[row][col]

            if num == target:
                return True
            elif num < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return False
