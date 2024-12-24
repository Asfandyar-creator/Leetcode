"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

Example 1:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
 

Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
 

Follow up: Could you use search pruning to make your solution faster with a larger board?
"""

class Solution(object):
    def exist(self, board, word):
        if not board or not board[0]:
            return False
        
        rows = len(board)
        cols = len(board[0])
        
        def dfs(r, c, index):
            # Found the word
            if index == len(word):
                return True
                
            # Check boundaries and if current cell matches required letter
            if (r < 0 or r >= rows or 
                c < 0 or c >= cols or 
                board[r][c] != word[index]):
                return False
                
            # Save current cell value
            temp = board[r][c]
            # Mark as visited by changing to '#'
            board[r][c] = '#'
            
            # Check all 4 directions
            result = (dfs(r+1, c, index+1) or  # down
                    dfs(r-1, c, index+1) or   # up
                    dfs(r, c+1, index+1) or   # right
                    dfs(r, c-1, index+1))     # left
            
            # Restore the cell value
            board[r][c] = temp
            
            return result
        
        # Try starting from each cell in the grid
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        
        return False
        