class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        n = len(source)
        
        trie = {}
        nodes_count = 0
        def get_id(s):
            nonlocal nodes_count
            curr = trie
            for char in s:
                if char not in curr:
                    curr[char] = {}
                curr = curr[char]
            if "id" not in curr:
                curr["id"] = nodes_count
                nodes_count += 1
            return curr["id"]

        # Collect unique substring lengths for DP optimization
        sub_lengths = set()
        for s in original: sub_lengths.add(len(s))
        for s in changed: sub_lengths.add(len(s))

        # 2. Build the distance matrix for Floyd-Warshall
        # We need enough space for all unique strings in original/changed
        all_unique = set(original) | set(changed)
        m = len(all_unique)
        dist = [[math.inf] * m for _ in range(m)]
        for i in range(m): dist[i][i] = 0

        for o, c, z in zip(original, changed, cost):
            u, v = get_id(o), get_id(c)
            dist[u][v] = min(dist[u][v], z)

        # Floyd-Warshall: O(m^3) where m <= 200 (2 * cost.length)
        for k in range(m):
            for i in range(m):
                if dist[i][k] == math.inf: continue
                for j in range(m):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        # 3. Dynamic Programming: dp[i] is min cost for prefix source[:i]
        dp = [math.inf] * (n + 1)
        dp[0] = 0

        for i in range(n):
            if dp[i] == math.inf: continue
            
            # Case 1: source[i] == target[i], no cost to skip
            if source[i] == target[i]:
                dp[i+1] = min(dp[i+1], dp[i])
            
            # Case 2: Match substrings in the trie
            # Optimization: Only check lengths that exist in our transformation rules
            for length in sub_lengths:
                if i + length <= n:
                    s_sub = source[i : i + length]
                    t_sub = target[i : i + length]
                    
                    # Manual trie lookup or string ID lookup
                    def find_id(s):
                        curr = trie
                        for char in s:
                            if char not in curr: return None
                            curr = curr[char]
                        return curr.get("id")

                    u, v = find_id(s_sub), find_id(t_sub)
                    if u is not None and v is not None:
                        cost_val = dist[u][v]
                        if cost_val != math.inf:
                            dp[i + length] = min(dp[i + length], dp[i] + cost_val)

        return dp[n] if dp[n] != math.inf else -1