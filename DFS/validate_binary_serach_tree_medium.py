"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left 
subtree
 of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:


Input: root = [2,1,3]
Output: true
Example 2:


Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1


"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        return self.validate(root, float('-inf'), float('inf'))
    
    def validate(self, node, min_val, max_val):
        if not node:
            return True  # An empty tree is a valid BST
        
        # Check if current node's value is within the allowed range
        if not (min_val < node.val < max_val):
            return False
        
        # Recursively check left and right subtrees
        return (self.validate(node.left, min_val, node.val) and
                self.validate(node.right, node.val, max_val))
