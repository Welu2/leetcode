class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for p in nums:
            if p == 2:
                ans.append(-1)
                continue
            
            for k in range(1, 32):
                if not (p & (1 << k)):
                    ans.append(p ^ (1 << (k - 1)))
                    break
        return ans