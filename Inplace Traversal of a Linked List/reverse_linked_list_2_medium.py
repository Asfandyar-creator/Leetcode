# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        # Edge case: If left == right, no need to reverse
        if left == right:
            return head

        # Create a dummy node to simplify the edge cases (like reversing from the first node)
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy 

        # Step 1: Traverse to the node just before the "left" position
        for _ in range(left - 1):
            prev = prev.next

        # Pointers to start reversal
        curr = prev.next
        next_node = None

        # Step 2: Reverse the sublist between left and right
        for _ in range(right - left):
            next_node = curr.next # Store next node
            curr.next = next_node.next # Remove next node from it's position
            next_node.next = prev.next # Insert next_node at the beginning of the next part
            prev.next = next_node # Move prev pointer to the new head of the reversed part

        # Step 3: Return the modified list    
        return dummy.next # The head might be different if we reversed from position 1