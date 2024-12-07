"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

"""


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # Initialize graph as an adjacency list and in-degree array
        graph = {i:[] for i in range(numCourses)}
        in_degree = [0] * numCourses

        # Build the in degree and graph
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1


        # Initialize a queue with courses having in-degree 0
        queue = []
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)

        visited_courses = 0  

        while queue:
            course = queue.pop(0)
            visited_courses += 1

            for neighbor in graph[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        return visited_courses == numCourses
