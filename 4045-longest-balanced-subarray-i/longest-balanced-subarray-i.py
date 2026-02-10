class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        max_length = 0
        n = len(nums)
        
        
        for i in range(n):
            
            evens = set()
            odds = set()
            
           
            for j in range(i, n):
                val = nums[j]
                
                
                if val % 2 == 0:
                    evens.add(val)
                else:
                    odds.add(val)
                
                
                if len(evens) == len(odds):
                  
                    max_length = max(max_length, j - i + 1)
                    
        return max_length