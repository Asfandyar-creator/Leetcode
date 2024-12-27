"""
Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. Return the output in any order.

 

Example 1:

Input: s = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]
Example 2:

Input: s = "3z4"
Output: ["3z4","3Z4"]
 
"""


class Solution(object):
    def letterCasePermutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []

        def backtrack(sub="", i=0):

            # If we've processed all the characters in string, add to result
            if i == len(s):
                result.append(sub)
                return
            # If current character is a digit, just add it
            if s[i].isdigit():
                backtrack(sub + s[i], i + 1)
            # If it's a letter try both cases
            else:
                backtrack(sub + s[i].lower(), i + 1)
                backtrack(sub + s[i].upper(), i + 1)
            
        backtrack()
        return result