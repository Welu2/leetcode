class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        mp = defaultdict(list)
        for a, b, c in allowed:
            mp[(a, b)].append(c)

        @lru_cache(None)
        def dfs(row: str) -> bool:
            if len(row) == 1:
                return True

            # collect candidate lists for each position of next row
            candidates = []
            for i in range(len(row) - 1):
                pair = (row[i], row[i+1])
                if pair not in mp:
                    return False
                candidates.append(mp[pair])

            # backtrack to generate all next rows
            def build_next(idx, curr):
                if idx == len(candidates):
                    return dfs("".join(curr))
                for ch in candidates[idx]:
                    curr.append(ch)
                    if build_next(idx + 1, curr):
                        return True
                    curr.pop()
                return False

            return build_next(0, [])

        return dfs(bottom)
