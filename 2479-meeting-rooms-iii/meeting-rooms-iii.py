class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
    
        # Min-heap for busy rooms: (end_time, room_id)
        busy = []
        
        # Min-heap for idle rooms (room numbers)
        idle = list(range(n))
        heapq.heapify(idle)
        
        # Count of meetings held in each room
        cnt = [0] * n
        
        for s, e in meetings:
            duration = e - s
            
            # Free up all rooms that have finished by time s
            while busy and busy[0][0] <= s:
                end_time, room_id = heapq.heappop(busy)
                heapq.heappush(idle, room_id)
            
            # Assign to an idle room if available
            if idle:
                room_id = heapq.heappop(idle)
                cnt[room_id] += 1
                heapq.heappush(busy, (e, room_id))
            else:
                # No idle room: delay until the earliest room becomes free
                earliest_end, room_id = heapq.heappop(busy)
                cnt[room_id] += 1
                new_end = earliest_end + duration
                heapq.heappush(busy, (new_end, room_id))
        
        # Find the room with the most meetings (lowest number in case of tie)
        ans = 0
        for i in range(n):
            if cnt[ans] < cnt[i]:
                ans = i
        return ans