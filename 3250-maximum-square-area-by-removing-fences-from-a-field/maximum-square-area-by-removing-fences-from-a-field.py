class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        def get_distances(fences, limit):
            
            lines = sorted(fences + [1, limit])
            dist_set = set()
            
            for i in range(len(lines)):
                for j in range(i + 1, len(lines)):
                    dist_set.add(lines[j] - lines[i])
            return dist_set

        h_dist = get_distances(hFences, m)
        v_dist = get_distances(vFences, n)
        
        common = h_dist.intersection(v_dist)
        if not common:
            return -1
        
        max_side = max(common)
        return (max_side * max_side) % (10**9 + 7)
            