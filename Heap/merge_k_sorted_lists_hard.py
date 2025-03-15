"""

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
 

Constraints:

k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104.
"""

import heapq

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        # Min heap to keep track of the smallest elements
        min_heap = []
        
        # Step 1: Push all the first nodes of the k lists into the heap
        for i, node in enumerate(lists):
            if node:  # Check if the list is not empty
                heapq.heappush(min_heap, (node.val, i, node))  # Store (value, index, node)

        # Step 2: Create a dummy node to build the merged linked list
        dummy = ListNode(0)
        current = dummy
        
        # Step 3: Extract min from heap and add the next node from the same list
        while min_heap:
            val, i, node = heapq.heappop(min_heap)  # Get the smallest node
            current.next = node  # Attach to result list
            current = current.next  # Move forward
            
            if node.next:  # If there are more nodes in the list, push next node to heap
                heapq.heappush(min_heap, (node.next.val, i, node.next))
        
        return dummy.next  # Return the merged sorted list
