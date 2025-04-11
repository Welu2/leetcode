class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph=defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        for ed in graph:
            if len(graph[ed]) == len(graph)-1:
                return ed