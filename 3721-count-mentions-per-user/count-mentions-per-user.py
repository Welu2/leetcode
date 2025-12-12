class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        events.sort(key=lambda e: (int(e[1]), 0 if e[0] == "OFFLINE" else 1))

        online = [True] * numberOfUsers
        reOnline = [None] * numberOfUsers
        mentions = [0] * numberOfUsers

        def update(t):
            for i in range(numberOfUsers):
                if reOnline[i] is not None and reOnline[i] <= t:
                    online[i] = True
                    reOnline[i] = None

        for typ, ts, data in events:
            ts = int(ts)
            update(ts)

            if typ == "OFFLINE":
                u = int(data)
                online[u] = False
                reOnline[u] = ts + 60
            else:
                tokens = data.split()
                if tokens == ["ALL"]:
                    for i in range(numberOfUsers):
                        mentions[i] += 1
                elif tokens == ["HERE"]:
                    for i in range(numberOfUsers):
                        if online[i]:
                            mentions[i] += 1
                else:
                    for tok in tokens:
                        if tok.startswith("id"):
                            mentions[int(tok[2:])] += 1

        return mentions