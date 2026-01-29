class Solution:
    def minimumPrefixLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        
    
        i = n - 1
        while i > 0 and nums[i-1] < nums[i]:
            i -= 1
            
        return i