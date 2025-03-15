"""
Given the head of a linked list, rotate the list to the right by k places.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Example 2:


Input: head = [0,1,2], k = 4
Output: [2,0,1]
 

Constraints:

The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        # Edge cases: If the list is empty or has only one node, return it as it is
        if not head or not head.next or k == 0:
            return head

        # Step 1: Compute the length of the list
        length = 1
        tail = head
        while tail.next: # Traverse to find the last node
            tail = tail.next
            length += 1
            

        # Step 2: Optimize k (if k is greater than length, reduce it)
        k = k % length
        if k == 0:
            return head # No rotation needed

        # Step 3: Make the list circular
        tail.next = head # Connect last node to first node to form a circle

        # Step 4: Find the new head (length - k steps from the current head)
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next # Move to the new tail
        
        new_head = new_tail.next # The next node will be the new head

        # Step 5: Break the circle
        new_tail.next = None

        return new_head 