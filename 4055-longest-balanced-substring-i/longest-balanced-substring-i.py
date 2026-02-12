class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        max_length = 0

        
        for i in range(n):
           
            counts = [0] * 26
            distinct_count = 0
            
            for j in range(i, n):
                char_idx = ord(s[j]) - ord('a')
                
                
                if counts[char_idx] == 0:
                    distinct_count += 1
                
                counts[char_idx] += 1
                
               
                current_len = j - i + 1
                
               
                if current_len % distinct_count == 0:
                    target_freq = current_len // distinct_count
                    
                   
                    is_balanced = True
                    for c in counts:
                        if c > 0 and c != target_freq:
                            is_balanced = False
                            break
                    
                    if is_balanced:
                        max_length = max(max_length, current_len)
                        
        return max_length