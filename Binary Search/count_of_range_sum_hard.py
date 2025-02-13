"""
Given an integer array nums and two integers lower and upper, return the number of range sums that lie in [lower, upper] inclusive.

Range sum S(i, j) is defined as the sum of the elements in nums between indices i and j inclusive, where i <= j.

 

Example 1:

Input: nums = [-2,5,-1], lower = -2, upper = 2
Output: 3
Explanation: The three ranges are: [0,0], [2,2], and [0,2] and their respective sums are: -2, -1, 2.
Example 2:

Input: nums = [0], lower = 0, upper = 0
Output: 1
 

Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
-105 <= lower <= upper <= 105
The answer is guaranteed to fit in a 32-bit integer.

"""

class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        from bisect import bisect_left, bisect_right

        def mergeSort(prefix, left, right):
            if left >= right:
                return 0
            
            mid = (left + right) // 2
            count = mergeSort(prefix, left, mid) + mergeSort(prefix, mid + 1, right)
            
            # Count valid sums using two pointers
            j, k = mid + 1, mid + 1
            for i in range(left, mid + 1):
                while k <= right and prefix[k] - prefix[i] < lower:
                    k += 1
                while j <= right and prefix[j] - prefix[i] <= upper:
                    j += 1
                count += (j - k)
            
            # Merge the sorted halves
            prefix[left:right + 1] = sorted(prefix[left:right + 1])
            return count

        # Compute prefix sums
        prefix_sums = [0]  # Start with 0 for easier calculations
        for num in nums:
            prefix_sums.append(prefix_sums[-1] + num)

        return mergeSort(prefix_sums, 0, len(prefix_sums) - 1)
