class Solution:
    def minimumDeletions(self, s: str) -> int:
        ans = 0
       
        b_count = 0
        
        for char in s:
            if char == 'b':
                b_count += 1
            else:
                ans = min(ans + 1, b_count)
                
        return ans
