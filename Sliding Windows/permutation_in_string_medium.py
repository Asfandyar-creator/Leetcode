"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.

"""
from collections import Counter
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        len_s1, len_s2 = len(s1), len(s2)

        if len_s1 > len_s2:
            return False # s1 can't be a permutation in s2 if it's longer

        s1_count = Counter(s1) # Frequence count of s1
        window_count = Counter(s2[:len_s1]) # Initial window of size len(s1)

        if s1_count == window_count:
            return True # Initial window is a match
        
        for i in range(len_s1, len_s2):
            # Add new character to window
            window_count[s2[i]] += 1
            # Remove the oldest character from the window
            window_count[s2[i - len_s1]] -= 1


            # If a character's count drops to 0, remove it from the dictionary
            if window_count[s2[i - len_s1]] == 0:
                del window_count[s2[i - len_s1]]

            # Compare frequence maps
            if s1_count == window_count:
                return True
        return False