class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        pos = defaultdict(list)
        for idx, x in enumerate(nums):
            pos[x].append(idx)

        ans = float("inf")

        for indices in pos.values():
            if len(indices) < 3:
                continue

            for t in range(len(indices) - 2):
                span = indices[t + 2] - indices[t]
                ans = min(ans, 2 * span)

        return -1 if ans == float("inf") else ans