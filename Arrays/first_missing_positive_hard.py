"""
Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

 

Example 1:

Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.
 

Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
"""

class Solution(object):
    def firstMissingPositive(self, nums):
        n = len(nums)
        
        # Step 1: Modify the array so that all numbers <= 0 become n+1
        # We do this because these numbers can't be the answer and we want to use
        # the array indices for marking presence
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1
        
        # Step 2: Mark presence of each number x by making nums[x-1] negative
        for i in range(n):
            num = abs(nums[i])  # Take absolute since number might be already negative
            if num <= n:  # Only mark if number is in valid range
                nums[num-1] = -abs(nums[num-1])
        
        # Step 3: Find first positive number
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        
        # If all numbers 1 to n exist, return n+1
        return n + 1