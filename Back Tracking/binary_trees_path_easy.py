"""
Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.

 

Example 1:
Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]
Example 2:

Input: root = [1]
Output: ["1"]
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        if not root:
            return []
        
        results = []

        def dfs(node, current_path):
            # Add current node's value to path
            if current_path:
                current_path += "->" + str(node.val)
            else:
                current_path = str(node.val)
            
            # If leaf node (no children), add to result
            if not node.left and not node.right:
                results.append(current_path)
                return
            
            # Recursively traverse subtrees
            if node.left:
                dfs(node.left, current_path)
            if node.right:
                dfs(node.right, current_path)

        dfs(root, "")
        return results