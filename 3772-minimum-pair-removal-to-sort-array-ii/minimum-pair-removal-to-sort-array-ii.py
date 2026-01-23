class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0

        
        nxt = list(range(1, n + 1))
        prv = list(range(-1, n - 1))
        
        
        inversions = 0
        pq = []
        
        def get_pair_info(i):
            
            if i < 0 or nxt[i] >= n:
                return None, False
            j = nxt[i]
            return (nums[i] + nums[j]), (nums[i] > nums[j])

        
        for i in range(n - 1):
            s, is_inv = get_pair_info(i)
            heapq.heappush(pq, (s, i))
            if is_inv:
                inversions += 1
        
        ops = 0
        
        exists = [True] * n
        
        while inversions > 0:
            s, i = heapq.heappop(pq)
            
            
            if not exists[i] or nxt[i] >= n or not exists[nxt[i]]:
                continue
            j = nxt[i]
            if nums[i] + nums[j] != s:
                continue
            
            # Perform merge operation
            ops += 1
            
            
            if prv[i] != -1:
                _, was_inv = get_pair_info(prv[i])
                if was_inv: inversions -= 1
            
            # Current pair being merged: (i, j)
            _, current_inv = get_pair_info(i)
            if current_inv: inversions -= 1
                
            # Neighbor to the right: (j, nxt[j])
            if nxt[j] < n:
                _, was_inv = get_pair_info(j)
                if was_inv: inversions -= 1

            nums[i] = s
            exists[j] = False
            new_next = nxt[j]
            nxt[i] = new_next
            if new_next < n:
                prv[new_next] = i
            
           
            if prv[i] != -1:
                new_s, is_inv = get_pair_info(prv[i])
                heapq.heappush(pq, (new_s, prv[i]))
                if is_inv: inversions += 1
            
            
            if nxt[i] < n:
                new_s, is_inv = get_pair_info(i)
                heapq.heappush(pq, (new_s, i))
                if is_inv: inversions += 1
                
        return ops