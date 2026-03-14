class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        happy_strings = []
    
        def backtrack(current_s):
           
            if len(current_s) == n:
                happy_strings.append(current_s)
                return
            
          
            for char in ['a', 'b', 'c']:
            
                if not current_s or current_s[-1] != char:
                    backtrack(current_s + char)
          
                    if len(happy_strings) == k:
                        return

        backtrack("")
        
        
        return happy_strings[k-1] if len(happy_strings) >= k else ""