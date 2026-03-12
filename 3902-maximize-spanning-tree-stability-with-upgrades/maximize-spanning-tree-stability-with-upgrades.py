class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        must_edges = []
        optional_edges = []
        scores = set()
        
        for u, v, s, m in edges:
            scores.add(s)
            if m == 1:
                must_edges.append((u, v, s))
            else:
                optional_edges.append((u, v, s))
                scores.add(s * 2)
                
        sorted_scores = sorted(list(scores))

        def can_achieve(min_score):
            parent = list(range(n))
            def find(i):
                if parent[i] == i: return i
                parent[i] = find(parent[i])
                return parent[i]
            
            def union(i, j):
                root_i, root_j = find(i), find(j)
                if root_i != root_j:
                    parent[root_i] = root_j
                    return True
                return False

            edges_count = 0
            
          
            for u, v, s in must_edges:
                if s < min_score: return False
                if not union(u, v): return False # Cycle in mandatory edges
                edges_count += 1
                
            
            upgradable = []
            for u, v, s in optional_edges:
                if s >= min_score:
                    if union(u, v):
                        edges_count += 1
                elif s * 2 >= min_score:
                    upgradable.append((u, v))
                    
          
            upgrades_used = 0
            for u, v in upgradable:
                if edges_count == n - 1: break
                if union(u, v):
                    edges_count += 1
                    upgrades_used += 1
                    
            return edges_count == n - 1 and upgrades_used <= k

      
        ans = -1
        low, high = 0, len(sorted_scores) - 1
        while low <= high:
            mid = (low + high) // 2
            if can_achieve(sorted_scores[mid]):
                ans = sorted_scores[mid]
                low = mid + 1
            else:
                high = mid - 1
                
        return ans