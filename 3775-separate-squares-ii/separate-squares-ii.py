class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        events = []
        xs = []

        # Build vertical events and x-coordinates
        for x, y, l in squares:
            x1, x2 = x, x + l
            y1, y2 = y, y + l
            events.append((y1, 1, x1, x2))   # add interval at bottom
            events.append((y2, -1, x1, x2))  # remove interval at top
            xs.append(x1)
            xs.append(x2)

        # Coordinate compression for x
        xs = sorted(set(xs))
        m = len(xs)

        # Segment tree over [0, m-2], each node represents [xs[i], xs[i+1]]
        cover = [0] * (4 * m)
        length = [0] * (4 * m)

        def update(idx, l, r, ql, qr, val):
            if qr <= l or r <= ql:
                return
            if ql <= l and r <= qr:
                cover[idx] += val
            else:
                mid = (l + r) // 2
                update(idx * 2, l, mid, ql, qr, val)
                update(idx * 2 + 1, mid, r, ql, qr, val)

            if cover[idx] > 0:
                length[idx] = xs[r] - xs[l]
            else:
                if l + 1 == r:
                    length[idx] = 0
                else:
                    length[idx] = length[idx * 2] + length[idx * 2 + 1]

        # Sort events by y
        events.sort()
        total_area = 0.0
        prev_y = events[0][0]
        i = 0
        n_events = len(events)

        # First sweep to compute total union area
        while i < n_events:
            y = events[i][0]
            dy = y - prev_y
            if dy > 0:
                total_area += length[1] * dy
                prev_y = y

            # process all events at this y
            while i < n_events and events[i][0] == y:
                _, typ, x1, x2 = events[i]
                l = bisect.bisect_left(xs, x1)
                r = bisect.bisect_left(xs, x2)
                update(1, 0, m - 1, l, r, typ)
                i += 1

        half = total_area / 2.0

        # Reset tree for second sweep
        cover = [0] * (4 * m)
        length = [0] * (4 * m)

        prev_y = events[0][0]
        i = 0
        acc_area = 0.0

        # Second sweep: stop when reaching half area
        while i < n_events:
            y = events[i][0]
            dy = y - prev_y
            if dy > 0:
                strip_area = length[1] * dy
                if acc_area + strip_area >= half - 1e-12 and length[1] > 0:
                    # line is inside this strip
                    remain = half - acc_area
                    offset = remain / length[1]
                    return prev_y + offset
                acc_area += strip_area
                prev_y = y

            # process all events at this y
            while i < n_events and events[i][0] == y:
                _, typ, x1, x2 = events[i]
                l = bisect.bisect_left(xs, x1)
                r = bisect.bisect_left(xs, x2)
                update(1, 0, m - 1, l, r, typ)
                i += 1

        # fallback (should not really happen if total_area > 0)
        return float(prev_y)