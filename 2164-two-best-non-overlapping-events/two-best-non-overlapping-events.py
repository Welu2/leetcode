class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x: x[0])
        n = len(events)

        starts = [e[0] for e in events]
        vals = [e[2] for e in events]

        # suffix max of values
        suffMax = [0] * n
        suffMax[-1] = vals[-1]
        for i in range(n - 2, -1, -1):
            suffMax[i] = max(vals[i], suffMax[i + 1])

        ans = 0
        for i in range(n):
            start, end, val = events[i]

            # first index with start >= end + 1 (non-overlapping)
            j = bisect_left(starts, end + 1)

            # take this event alone
            best = val
            # or combine with best future event
            if j < n:
                best = val + suffMax[j]

            ans = max(ans, best)

        return ans