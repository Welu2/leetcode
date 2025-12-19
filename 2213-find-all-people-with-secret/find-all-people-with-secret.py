class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        has_secret = [False] * n
        has_secret[0] = True
        has_secret[firstPerson] = True

        
        meetings.sort(key=lambda x: x[2])

        i = 0
        m = len(meetings)

        while i < m:
            t = meetings[i][2]

            
            graph = defaultdict(list)
            people = set()

            while i < m and meetings[i][2] == t:
                x, y, _ = meetings[i]
                graph[x].append(y)
                graph[y].append(x)
                people.add(x)
                people.add(y)
                i += 1

            
            q = deque()
            visited = set()

            for p in people:
                if has_secret[p]:
                    q.append(p)
                    visited.add(p)

            
            while q:
                cur = q.popleft()
                for nei in graph[cur]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append(nei)

            
            for p in visited:
                has_secret[p] = True

        return [i for i in range(n) if has_secret[i]]
            