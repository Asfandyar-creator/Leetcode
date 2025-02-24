"""
Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.

 

Example 1:

Input: s = "aab"
Output: "aba"
Example 2:

Input: s = "aaab"
Output: ""
 

Constraints:

1 <= s.length <= 500
s consists of lowercase English letters.

"""

from collections import Counter
import heapq
class Solution(object):
    def reorganizeString(self, s):
          # Step 1: Count character frequencies
        freq = Counter(s)
        
        # Step 2: Check if rearrangement is possible
        max_freq = max(freq.values())
        if max_freq > (len(s) + 1) // 2:
            return ""
        
        # Step 3: Use a max heap (Python has a min heap, so we use negative values)
        max_heap = [(-count, char) for char, count in freq.items()]
        heapq.heapify(max_heap)
        
        # Step 4: Build the result using a greedy approach
        result = []
        prev_count, prev_char = 0, ""
        
        while max_heap:
            count, char = heapq.heappop(max_heap)  # Get most frequent char
            result.append(char)
            
            # If the previous character still has remaining count, push it back
            if prev_count < 0:
                heapq.heappush(max_heap, (prev_count, prev_char))
            
            # Update previous character info
            prev_count, prev_char = count + 1, char  # Decrease count (closer to 0)
        
        return "".join(result)