class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        def can_reduce(time_limit):
            total_reduced = 0
            for w in workerTimes:
                
                x = int((-1 + math.sqrt(1 + 8 * time_limit / w)) / 2)
                total_reduced += x
                if total_reduced >= mountainHeight:
                    return True
            return total_reduced >= mountainHeight

        low = 0
       
        high = min(workerTimes) * mountainHeight * (mountainHeight + 1) // 2
        
        ans = high
        while low <= high:
            mid = (low + high) // 2
            if can_reduce(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans