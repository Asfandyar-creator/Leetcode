"""
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

 

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length

"""
from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []


        dq = deque() # Store indices, ensuring the deque is in decreasing order
        result = []

        for i in range(len(nums)):
            # Remove elements out of the window
            if dq and dq[0] < i - k + 1:
                dq.popleft()

            
            # Remove elements similar that tne current one
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            
            # Insert current element index
            dq.append(i)

            # Append the maximum of the window (start from index k - 1)
            if i >= k - 1:
                result.append(nums[dq[0]])
        
        return result