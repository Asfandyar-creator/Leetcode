"""

Given an integer array nums, return the maximum result of nums[i] XOR nums[j], where 0 <= i <= j < n.

 

Example 1:

Input: nums = [3,10,5,25,2,8]
Output: 28
Explanation: The maximum result is 5 XOR 25 = 28.
Example 2:

Input: nums = [14,70,53,83,49,91,36,80,92,51,66,70]
Output: 127
 

Constraints:

1 <= nums.length <= 2 * 105
0 <= nums[i] <= 231 - 1
Seen this question in a real interview before?
1/5
"""

class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_xor = 0
        mask = 0

        for i in range(31, -1, -1): # Check bits from MSB to LSB
            mask |= (1 << i)
            prefixes = {num & mask for num in nums} # Store prefixes of nums


            candidate = max_xor | (1 << i) # Possible max XOR

            for prefix in prefixes:
                if candidate ^ prefix in prefixes: # Check if we can achieve this XOR
                    max_xor = candidate
                    break # Found max XOR for this bit positon 
        return max_xor