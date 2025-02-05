"""
Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

You must find a solution with a memory complexity better than O(n2).

 

Example 1:

Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13
Example 2:

Input: matrix = [[-5]], k = 1
Output: -5
 

Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 300
-109 <= matrix[i][j] <= 109
All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
1 <= k <= n2

"""


class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)
        low, high = matrix[0][0], matrix[n-1][n-1]
        
        def countLessEqual(mid):
            """Counts how many numbers in the matrix are ≤ mid"""
            count = 0
            row, col = n - 1, 0  # Start from bottom-left corner
            
            while row >= 0 and col < n:
                if matrix[row][col] <= mid:
                    count += row + 1  # All elements above this are also ≤ mid
                    col += 1  # Move right
                else:
                    row -= 1  # Move up
            
            return count
        
        # Binary search in the sorted value range
        while low < high:
            mid = (low + high) // 2
            if countLessEqual(mid) < k:
                low = mid + 1  # Need more elements, move right
            else:
                high = mid  # Mid could be the answer
        
        return low  # The k-th smallest element

