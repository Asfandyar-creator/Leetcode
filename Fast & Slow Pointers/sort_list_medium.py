"""
Given the head of a linked list, return the list after sorting it in ascending order.

 

Example 1:


Input: head = [4,2,1,3]
Output: [1,2,3,4]
Example 2:


Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is in the range [0, 5 * 104].
-105 <= Node.val <= 105
 

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?

"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head # Base case empty list or single node
        

        # Function to find middle node using slow and fast pointers
        def get_middle(node):
            slow, fast = node, node.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            
            return slow

        
        # Function to merge two sorted lists
        def merge(l1, l2):
            dummy = ListNode()
            tail = dummy
            while l1 and l2:
                if l1.val < l2.val:
                    tail.next, l1 = l1, l1.next

                else:
                    tail.next, l2 = l2, l2.next
                tail = tail.next
            tail.next = l1 if l1 else l2 # Append the remaining elements
            return dummy.next


        # Find the middle and split the list
        mid = get_middle(head)
        right_head = mid.next
        mid.next = None # Split the list into two halves


        # Recursively sort both halves
        left_sorted = self.sortList(head)
        right_sorted = self.sortList(right_head)


        # Merge the sorted halves
        return merge(left_sorted, right_sorted)