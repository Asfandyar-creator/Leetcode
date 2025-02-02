"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

 

Example 1:


Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
Example 2:

Input: n = 1
Output: [["Q"]]

"""

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        results = []
        board = ["." * n for _ in range(n)]
        cols = set()
        posDiags = set()  # (row + col)
        negDiags = set()  # (row - col)
        
        def backtrack(r):
            if r == n:
                results.append(board[:])
                return
            
            for c in range(n):
                if c in cols or (r + c) in posDiags or (r - c) in negDiags:
                    continue
                
                board[r] = board[r][:c] + 'Q' + board[r][c+1:]
                cols.add(c)
                posDiags.add(r + c)
                negDiags.add(r - c)
                
                backtrack(r + 1)
                
                board[r] = board[r][:c] + '.' + board[r][c+1:]
                cols.remove(c)
                posDiags.remove(r + c)
                negDiags.remove(r - c)
        
        backtrack(0)
        return results