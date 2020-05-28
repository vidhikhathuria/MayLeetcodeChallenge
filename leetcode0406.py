# Problem Link : https://leetcode.com/problems/possible-bipartition/

class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        def bipartite(edges, color, node, N):
            q = []
            q.append(node)
            color[node] = 1
            while len(q):
                # print(color)
                curr = q.pop(0)
                for i in edges[curr]:
                    # print(i, curr)
                    if color[i] == color[curr]:
                        return False
                    if color[i] == -1:
                        color[i] = 1 - color[curr]
                        q.append(i)
            return True
        
        
        from collections import defaultdict
        edges = defaultdict(set)
        for i in dislikes:
            edges[i[0]].add(i[1])
            edges[i[1]].add(i[0])
        color = [-1] * (N + 1)
        for i in range(1, N):
            # print(color)
            if color[i] == -1:
                if not bipartite(edges, color, i, N):
                    return False
        return True