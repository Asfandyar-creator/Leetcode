"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8

"""

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []

        def backtrack(open_count, close_count, path):
            if open_count == n and close_count == n:
                result.append("".join(path))  # Found a valid combination
                return
            if open_count < n:  # Add '(' if we haven't reached the limit
                path.append('(')
                backtrack(open_count + 1, close_count, path)
                path.pop()  # Backtrack
            if close_count < open_count:  # Add ')' only if there's an unmatched '('
                path.append(')')
                backtrack(open_count, close_count + 1, path)
                path.pop()  # Backtrack

        backtrack(0, 0, [])
        return result
