"""
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
 

Follow up: Could you find an algorithm that runs in O(m + n) time?

"""
from collections import Counter
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return ""

        # Step 1: Count occurence of each character i   n t
        t_count = Counter(t)
        window_count = {}

        required = len(t_count) # Number of unique charts in t that must be in the window
        formed = 0 # Number of unique chars in window that match required frequence

        left, right = 0, 0
        min_len = float("inf")
        min_window = ""

        while right < len(s):
            # Add current character to window_count
            char = s[right]
            window_count[char] = window_count.get(char, 0) + 1

            # If the frequence matches t's required frequency, increase formed count
            if char in t_count and window_count[char] == t_count[char]:
                formed += 1
            
            # Contract the window while it's valid
            while left <= right and formed == required:
                # Update minimum window
                if (right - left + 1) < min_len:
                    min_len = right - left + 1
                    min_window = s[left : right +1]
                
                # Remove the leftmost character from window_count
                left_char =  s[left]
                window_count[left_char] -= 1
                if left_char in t_count and window_count[left_char] < t_count[left_char]:
                    formed -= 1 # We no longer have the required count

                
                left += 1 # Move left pointer
            right += 1 # Expand window 

        return min_window