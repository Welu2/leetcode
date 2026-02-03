class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 4: return False
        
        idx = 0
      
        while idx + 1 < n and nums[idx] < nums[idx+1]:
            idx += 1
        if idx == 0 or idx == n - 1: return False 
        
        
        p = idx 
        while idx + 1 < n and nums[idx] > nums[idx+1]:
            idx += 1
        if idx == p or idx == n - 1: return False 
        
       
        q = idx 
        while idx + 1 < n and nums[idx] < nums[idx+1]:
            idx += 1
            
        return idx == n - 1 
