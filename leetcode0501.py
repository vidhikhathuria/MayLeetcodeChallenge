# Problem Link: https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict
        queue = [i for i in range(numCourses)]
        indegree = [0 for i in range(numCourses)]
        d = defaultdict(list)
        for i in prerequisites:
            if i[1] in queue:
                queue.remove(i[1])
            indegree[i[1]] += 1
            d[i[0]].append(i[1])
        
        c = 0
        while queue:
            u = queue.pop(0)
            for i in d[u]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)
            c += 1
        # print(c, numCourses)
        if c != numCourses:
            return False
        return True