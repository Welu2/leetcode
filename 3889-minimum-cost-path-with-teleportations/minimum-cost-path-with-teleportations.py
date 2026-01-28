class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        INF = float('inf')

        # dist[r][c][t] = min cost to reach (r,c) using t teleports
        dist = [[[INF] * (k + 1) for _ in range(n)] for _ in range(m)]
        dist[0][0][0] = 0

        # All cells sorted by value
        cells = []
        for i in range(m):
            for j in range(n):
                cells.append((grid[i][j], i, j))
        cells.sort()

        used = [0] * (k + 1)

        pq = [(0, 0, 0, 0)]  # cost, r, c, teleports_used

        while pq:
            cost, r, c, t = heapq.heappop(pq)
            if cost > dist[r][c][t]:
                continue

            if r == m - 1 and c == n - 1:
                return cost

            # Normal moves
            if r + 1 < m:
                nc = cost + grid[r + 1][c]
                if nc < dist[r + 1][c][t]:
                    dist[r + 1][c][t] = nc
                    heapq.heappush(pq, (nc, r + 1, c, t))

            if c + 1 < n:
                nc = cost + grid[r][c + 1]
                if nc < dist[r][c + 1][t]:
                    dist[r][c + 1][t] = nc
                    heapq.heappush(pq, (nc, r, c + 1, t))

            
            if t < k:
                curr_val = grid[r][c]
                idx = used[t]

                while idx < len(cells) and cells[idx][0] <= curr_val:
                    _, nr, nc = cells[idx]
                    if cost < dist[nr][nc][t + 1]:
                        dist[nr][nc][t + 1] = cost
                        heapq.heappush(pq, (cost, nr, nc, t + 1))
                    idx += 1

                used[t] = idx

        return -1