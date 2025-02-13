"""
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

 

Example 1:


Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true
Example 2:


Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false

"""

#Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root, subRoot):
        # If the main tree is empty, there is no subtree to compare
        if not root:
            return False
        
        # If the trees are identical at the current node, return True.
        if self.isSameTree(root, subRoot):
            return True
        
        # Otherwise, check the left and right subtrees recursively.
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def isSameTree(self, s, t):
        # If both trees are empty, they are the same.
        if not s and not t:
            return True
        # If one of them is empty or the values do not match, they are not the same.
        if not s or not t or s.val != t.val:
            return False
        
        # Recursively check the left and right subtrees.
        return self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)