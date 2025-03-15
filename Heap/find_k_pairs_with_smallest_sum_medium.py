"""
You are given two integer arrays nums1 and nums2 sorted in non-decreasing order and an integer k.

Define a pair (u, v) which consists of one element from the first array and one element from the second array.

Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.

 

Example 1:

Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
Example 2:

Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [[1,1],[1,1]]
Explanation: The first 2 pairs are returned from the sequence: [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
 

Constraints:

1 <= nums1.length, nums2.length <= 105
-109 <= nums1[i], nums2[i] <= 109
nums1 and nums2 both are sorted in non-decreasing order.
1 <= k <= 104
k <= nums1.length * nums2.length

"""

import heapq
class Solution(object):

    def kSmallestPairs(self, nums1, nums2, k):
        if not nums1 or not nums2:
            return []
        
        min_heap = []
        result = []

        # Step 1: Push the first k pairs using nums1[0] and different nums2[j]
        for j in range(min(k, len(nums2))):  # We only need the first k elements from nums2
            heapq.heappush(min_heap, (nums1[0] + nums2[j], 0, j))  # Store (sum, index1, index2)

        # Step 2: Extract k smallest pairs
        while min_heap and len(result) < k:
            sum_val, i, j = heapq.heappop(min_heap)  # Get the smallest sum pair
            result.append([nums1[i], nums2[j]])  # Store the actual pair

            # Step 3: Push the next possible pair
            if i + 1 < len(nums1):  # Move to the next element in nums1 with the same nums2[j]
                heapq.heappush(min_heap, (nums1[i+1] + nums2[j], i+1, j))

        return result
