"""
You have k lists of sorted integers in non-decreasing order. Find the smallest range that includes at least one number from each of the k lists.

We define the range [a, b] is smaller than range [c, d] if b - a < d - c or a < c if b - a == d - c.

 

Example 1:

Input: nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
Output: [20,24]
Explanation: 
List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
List 2: [0, 9, 12, 20], 20 is in range [20,24].
List 3: [5, 18, 22, 30], 22 is in range [20,24].
Example 2:

Input: nums = [[1,2,3],[1,2,3],[1,2,3]]
Output: [1,1]
 

Constraints:

nums.length == k
1 <= k <= 3500
1 <= nums[i].length <= 50
-105 <= nums[i][j] <= 105
nums[i] is sorted in non-decreasing order.

"""

import heapq

class Solution:
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        min_heap = []
        max_value = float('-inf')  # Track the max value in the current range
        
        # Step 1: Insert the first element from each list into the heap
        for i in range(len(nums)):
            heapq.heappush(min_heap, (nums[i][0], i, 0))  # (value, list_index, element_index)
            max_value = max(max_value, nums[i][0])  # Track max value
        
        smallest_range = [float('-inf'), float('inf')]
        
        # Step 2: Expand the window
        while len(min_heap) == len(nums):  # Ensure all lists contribute
            min_value, row, col = heapq.heappop(min_heap)  # Get the smallest element
            
            # Update smallest range if the new one is smaller
            if max_value - min_value < smallest_range[1] - smallest_range[0]:
                smallest_range = [min_value, max_value]
            
            # Move to the next element in the same row (list)
            if col + 1 < len(nums[row]):
                next_value = nums[row][col + 1]
                heapq.heappush(min_heap, (next_value, row, col + 1))
                max_value = max(max_value, next_value)  # Update max value
            else:
                break  # If any list is exhausted, we cannot cover all lists anymore
        
        return smallest_range
