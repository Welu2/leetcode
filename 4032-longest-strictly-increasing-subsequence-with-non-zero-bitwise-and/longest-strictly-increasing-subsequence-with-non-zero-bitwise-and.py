class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        def get_lis(arr):
            if not arr: return 0
            tails = []
            for x in arr:
                idx = bisect.bisect_left(tails, x)
                if idx < len(tails):
                    tails[idx] = x
                else:
                    tails.append(x)
            return len(tails)
        
        max_len = 0
        for b in range(31):
            subset = [x for x in nums if (x >> b) & 1]
            if subset:
                max_len = max(max_len, get_lis(subset))
        return max_len