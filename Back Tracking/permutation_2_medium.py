"""
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

 

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 

"""


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()  # Step 1: Sort to detect duplicates
        used = [False] * len(nums)  # Track used elements

        def backtrack(currentPermutation):
            # Base case: if permutation is complete, add to result
            if len(currentPermutation) == len(nums):
                result.append(list(currentPermutation))
                return

            for i in range(len(nums)):
                # Skip used elements
                if used[i]:
                    continue
                
                # Skip duplicates: if nums[i] == nums[i-1] and previous was not used
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                
                # Choose: Mark as used and add to permutation
                used[i] = True
                currentPermutation.append(nums[i])
                
                # Explore: Recursively call backtrack
                backtrack(currentPermutation)
                
                # Unchoose: Remove last element and mark unused
                currentPermutation.pop()
                used[i] = False

        backtrack([])  # Start with an empty permutation
        return result
