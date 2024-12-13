"""
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

 

Example 1:

Input: root = [1,2,3,null,5,null,4]

Output: [1,3,4]

Explanation:

Example 2:

Input: root = [1,2,3,4,null,null,null,5]

Output: [1,3,4,5]

Explanation:

Example 3:

Input: root = [1,null,3]

Output: [1,3]

Example 4:

Input: root = []

Output: []
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        if not root:
            return []
        
        result = []
        # Start with root in queue
        queue = [root]
        
        while queue:
            size = len(queue)
            # Process each level
            for i in range(size):
                node = queue.pop(0)
                
                # Add left child to queue BEFORE right child
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
                # If this is last node in level, add its VALUE (not the node itself)
                if i == size - 1:
                    result.append(node.val)
        
        return result