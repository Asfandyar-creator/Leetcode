"""

Given an array nums of distinct integers, return all the possible 
permutations
. You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
 

Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
"""

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []

        def backtrack(currentPermutation, remainingNums):
            # Base case: if no numbers are remaining, add a copy of the current permutation to the result.
            if not remainingNums:
                result.append(list(currentPermutation))
                return
            
            # Iterate through the remaining numbers.
            for i in range(len(remainingNums)):
                # Choose: Add the number at index i to the current permutation.
                currentPermutation.append(remainingNums[i])
                # Explore: Recursively call backtrack with the updated permutation and remaining numbers.
                backtrack(currentPermutation, remainingNums[:i] + remainingNums[i+1:])
                # Unchoose (Backtrack): Remove the last added number to try another possibility.
                currentPermutation.pop()
        
        # Initialize the backtracking with an empty currentPermutation and the full nums list.
        backtrack([], nums)
        return result
