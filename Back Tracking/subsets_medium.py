"""
Given an integer array nums of unique elements, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]

"""

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        def backtrack(start=0, curr=[]): # Start with empty subset
            # Add current subset to the result
            result.append(curr[:])
            # Try adding each number
            for i in range(start, len(nums)):
                curr.append(nums[i]) # Include current number
                backtrack(i + 1, curr) # Generate numbers after i
                curr.pop() # Backtrack by removing the last number
        
        backtrack()
        return result