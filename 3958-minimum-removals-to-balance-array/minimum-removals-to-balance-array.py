class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
    
        n = len(nums)
        left = 0
        max_balanced_len = 0
     
        for right in range(n):
            # If the balance condition is violated, move the left pointer
            while nums[right] > nums[left] * k:
                left += 1
            
            # Calculate the length of the current balanced window
            current_len = right - left + 1
            max_balanced_len = max(max_balanced_len, current_len)
                
        
        return n - max_balanced_len