class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0
        carry = 0
        
        
        for i in range(len(s) - 1, 0, -1):
            digit = int(s[i]) + carry
            
            if digit == 1:
              
                steps += 2
                carry = 1
            else:
                # It's even: just divide by 2 (1 step).
                steps += 1
            
        return steps + carry