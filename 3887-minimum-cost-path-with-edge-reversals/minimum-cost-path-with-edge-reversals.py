class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
            adj = [[] for _ in range(n)]
            rev_adj = [[] for _ in range(n)]
            
            for u, v, w in edges:
                adj[u].append((v, w))
                rev_adj[v].append((u, w))
            
            dist = [float('inf')] * n
            dist[0] = 0
            pq = [(0, 0)]
            
            while pq:
                d, u = heapq.heappop(pq)
                
                if d > dist[u]:
                    continue
                
                if u == n - 1:
                    return d
                    
                for v, w in adj[u]:
                    if d + w < dist[v]:
                        dist[v] = d + w
                        heapq.heappush(pq, (dist[v], v))
                
                for v, w in rev_adj[u]:
                    if d + 2 * w < dist[v]:
                        dist[v] = d + 2 * w
                        heapq.heappush(pq, (dist[v], v))
                        
            return -1