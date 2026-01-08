class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        dp = [[-float('inf')] * m for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                current_prod = nums1[i] * nums2[j]
                prev_best = dp[i-1][j-1] if i > 0 and j > 0 else 0
                
                # Option 1: Start new or extend with current pair
                dp[i][j] = current_prod + max(0, prev_best)
                
                # Option 2: Skip current element from nums1
                if i > 0:
                    dp[i][j] = max(dp[i][j], dp[i-1][j])
                
                # Option 3: Skip current element from nums2
                if j > 0:
                    dp[i][j] = max(dp[i][j], dp[i][j-1])
                    
        return dp[n-1][m-1]