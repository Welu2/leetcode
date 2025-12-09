class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        left = defaultdict(int)
        right = defaultdict(int)
        MOD=10**9+7
        
        for x in nums:
            right[x] += 1
        
        ans = 0
        
        for j, x in enumerate(nums):
            
            right[x] -= 1
          
            target = 2 * x
            leftWays = left[target]
            rightWays = right[target]
            
            ans = (ans + leftWays * rightWays) % MOD
            
            
            left[x] += 1
        
        return ans