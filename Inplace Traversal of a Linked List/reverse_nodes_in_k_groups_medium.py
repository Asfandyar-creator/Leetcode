"""
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
Example 2:


Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
 

Constraints:

The number of nodes in the list is n.
1 <= k <= n <= 5000
0 <= Node.val <= 1000
 

Follow-up: Can you solve the problem in O(1) extra memory space?

"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        if not head or k == 1:
            return head  # No need to reverse if k is 1 or list is empty

        # Dummy node to simplify edge cases
        dummy = ListNode(0)
        dummy.next = head
        prev_group_end = dummy
        
        while True:
            # Step 1: Check if there are at least k nodes left
            kth_node = prev_group_end
            for _ in range(k):
                kth_node = kth_node.next
                if not kth_node:  # Not enough nodes left, break out
                    return dummy.next
            
            # Step 2: Reverse k nodes
            prev, curr = None, prev_group_end.next
            next_group_start = kth_node.next  # Store the next group's start node
            
            for _ in range(k):  # Reverse exactly k nodes
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            # Step 3: Connect reversed part with the previous and next parts
            start_of_reversed_group = prev  # This is now the new head of reversed k-group
            end_of_reversed_group = prev_group_end.next  # The old head becomes the new tail
            
            prev_group_end.next = start_of_reversed_group  # Link previous part to new head
            end_of_reversed_group.next = next_group_start  # Link reversed part to the rest of the list
            
            # Move prev_group_end forward to prepare for the next reversal
            prev_group_end = end_of_reversed_group
