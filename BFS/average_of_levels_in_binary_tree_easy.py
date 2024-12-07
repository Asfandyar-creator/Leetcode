"""
Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.
 

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [3.00000,14.50000,11.00000]
Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
Hence return [3, 14.5, 11].
Example 2:
Input: root = [3,9,20,15,7]
Output: [3.00000,14.50000,11.00000]
"""

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return []
        
        result = []
        queue = [root]  # Start with root node
        
        while queue:
            new_queue = []  # Store next level nodes
            sum_level = 0.0  # Use float for sum
            size = len(queue)
            
            # Process current level
            for node in queue:
                sum_level += float(node.val)  # Convert to float
                
                # Add children to next level queue
                if node.left:
                    new_queue.append(node.left)
                if node.right:
                    new_queue.append(node.right)
            
            # Append average of current level to result
            result.append(sum_level / size)
            queue = new_queue  # Update queue for next level
            
        return result