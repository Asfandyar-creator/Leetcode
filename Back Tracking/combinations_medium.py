"""
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.

 

Example 1:

Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
Example 2:

Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.
 

Constraints:

1 <= n <= 20
1 <= k <= n

"""

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []

        def backtrack(start, currentCombination):
            # Base case: when the combination size reaches k
            if len(currentCombination) == k:
                result.append(list(currentCombination))
                return
            
            # Iterate from the current number to n
            for i in range(start, n + 1):
                # Choose the number i
                currentCombination.append(i)
                # Explore with i+1 to avoid duplicates and maintain order
                backtrack(i + 1, currentCombination)
                # Unchoose (Backtrack) to try the next number
                currentCombination.pop()
        
        # Start backtracking from number 1
        backtrack(1, [])
        return result
