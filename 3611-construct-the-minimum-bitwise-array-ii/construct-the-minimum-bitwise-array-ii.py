class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for n in nums:
            # If the number is 2, no non-negative x satisfies x | (x + 1) == 2
            if n == 2:
                ans.append(-1)
                continue
            
            # Find the highest bit k such that all bits from 0 to k are 1
            k = 0
            while (n >> (k + 1)) & 1:
                if (n & (1 << (k + 1))):
                    k += 1
                else:
                    break
            
            # To minimize ans[i], we flip the highest bit k that is part of the 
            # contiguous trailing 1s block.
            ans.append(n ^ (1 << k))
        return ans