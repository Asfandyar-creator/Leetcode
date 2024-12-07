"""
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.


Example 1:
Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
[0,4]: [0,4] -> Pacific Ocean 
       [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean 
       [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
       [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
       [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific Ocean 
       [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean 
       [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean 
       [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.
Example 2:

Input: heights = [[1]]
Output: [[0,0]]
Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.
"""





class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        if not heights or not heights[0]:
             return []

        # Initialize queues for both oceans
        pacific_queue = [] # Cells touching pacific
        atlantic_queue = [] # Cells touching atlantic

        rows, cols = len(heights), len(heights[0])


        # Add Pacific edge cells (top row and left column)
        for i in range(rows):
            pacific_queue.append((i, 0)) # Left Edge
            atlantic_queue.append((i, cols - 1)) # Right Edge
        for j in range(cols):
            pacific_queue.append((0, j)) # Top Edge
            atlantic_queue.append((rows-1, j)) # Bottom Edge
        
        def bfs(queue):
            reachable = set(queue) # Cells that can reach this ocean

            # Process cells level by level
            while queue:
                row, col = queue.pop(0)

                # Check all four directions
                for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                    new_row, new_col = row + dx, col + dy

                    # Skip if:
                    # 1: Out of bounds
                    # 2: Already Processed
                    # 3: Water cannot flow (new cell is lower)
                    if (new_row < 0 or new_row >= rows or
                        new_col < 0 or new_col >= cols or
                        (new_row, new_col) in reachable or
                        heights[new_row][new_col] < heights[row][col]):
                        continue



                    queue.append((new_row, new_col))
                    reachable.add((new_row, new_col))
            
            return reachable

            # Find all cells that can reach each ocean
        pacific_reachable = bfs(pacific_queue)
        atlantic_reachable = bfs(atlantic_queue)
        
        # Return intersection as list of coordinates
        return [[r, c] for r, c in pacific_reachable.intersection(atlantic_reachable)]

                
