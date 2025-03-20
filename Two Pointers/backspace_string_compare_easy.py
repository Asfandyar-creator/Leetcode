"""
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

 

Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
Example 3:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".
 

Constraints:

1 <= s.length, t.length <= 200
s and t only contain lowercase letters and '#' characters.
 

Follow up: Can you solve it in O(n) time and O(1) space?

"""

class Solution(object):
    def backspaceCompare(self, s, t):
        def get_next_valid_index(string, index):
            skip = 0
            while index >= 0:
                if string[index] == '#':
                    skip += 1
                    index -= 1
                elif skip > 0:
                    skip -= 1
                    index -= 1
                else:
                    return index
            return -1  # No valid character left

        i, j = len(s) - 1, len(t) - 1

        while i >= 0 or j >= 0:
            i = get_next_valid_index(s, i)
            j = get_next_valid_index(t, j)

            if i >= 0 and j >= 0 and s[i] != t[j]:  # Compare valid characters
                return False
            if (i >= 0) != (j >= 0):  # If one string is finished but the other isn't
                return False

            i -= 1
            j -= 1

        return True
