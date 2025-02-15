"""
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

 

Example 1:


Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
Example 2:


Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
 

Constraints:

The number of nodes in the tree is in the range [1, 3 * 104].
-1000 <= Node.val <= 1000

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.max_sum = float('-inf')  # Stores the global maximum path sum
        
        def dfs(node):
            if not node:
                return 0  # If node is None, return 0 (ignore negative paths)

            # Compute the max path sum for the left and right children
            left_max = max(dfs(node.left), 0)  # Ignore negative contributions
            right_max = max(dfs(node.right), 0)

            # Update the global max_sum if the path including this node is larger
            self.max_sum = max(self.max_sum, left_max + node.val + right_max)

            # Return max sum for one side (either left or right) to continue the path
            return node.val + max(left_max, right_max)

        dfs(root)  # Start DFS from the root
        return self.max_sum
