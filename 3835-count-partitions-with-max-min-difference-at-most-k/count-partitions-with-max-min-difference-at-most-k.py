class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        n = len(nums)
        MOD=10**9+7
        
        dp = [0] * n
       
        pref = [0] * n

        maxdq = deque()  
        mindq = deque()  

        l = 0
        for r in range(n):
           
            while maxdq and nums[maxdq[-1]] <= nums[r]:
                maxdq.pop()
            maxdq.append(r)

            while mindq and nums[mindq[-1]] >= nums[r]:
                mindq.pop()
            mindq.append(r)

            while nums[maxdq[0]] - nums[mindq[0]] > k:
                l += 1
                # pop indices that are out of window
                if maxdq[0] < l:
                    maxdq.popleft()
                if mindq[0] < l:
                    mindq.popleft()

            # now window [l..r] is minimal valid window ending at r
            if l == 0:
                # segments can start at any j in [0..r]
                if r == 0:
                    dp[r] = 1
                else:
                    dp[r] = (pref[r-1] + 1) % MOD
            else:
             
                if l - 2 >= 0:
                    dp[r] = (pref[r-1] - pref[l-2]) % MOD
                else:
                    
                    dp[r] = pref[r-1] % MOD

            
            if r == 0:
                pref[r] = dp[r]
            else:
                pref[r] = (pref[r-1] + dp[r]) % MOD

        return dp[-1] % MOD
