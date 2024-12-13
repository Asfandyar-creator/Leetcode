"""
Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.

You can return the answer in any order.

 

Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
Output: [7,4,1]
Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.
Example 2:

Input: root = [1], target = 1, k = 3
Output: []
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        # Step 1: Build parent pointers

        parent = {}
        def dfs(node, par=None):
            if node:
                parent[node] = par
                dfs(node.left, node)
                dfs(node.right, node)
        dfs(root)

        # Step 2: BFS from target
        queue = [(target, 0)]
        seen = {target}
        result = []

        while queue:
            node, dist = queue.pop(0)

            # If we reached to the distance k, add it to result
            if dist == k:
                result.append(node.val)


            # Add all adjacent nodes (left, right, parent)
            for next_node in [node.left, node.right, parent[node]]:
                if next_node and next_node not in seen and dist + 1<= k:
                    seen.add(next_node)
                    queue.append((next_node, dist + 1))


        return result