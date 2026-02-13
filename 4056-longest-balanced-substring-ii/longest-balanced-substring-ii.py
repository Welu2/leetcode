class Solution:
    def longestBalanced(self, s: str) -> int:
        max_len = 0
        chars = ['a', 'b', 'c']
        
        
        for i in range(1, 8):
            subset = [chars[j] for j in range(3) if (i >> j) & 1]
            subset_set = set(subset)
            forbidden = set(chars) - subset_set
            
            
            segments = "".join([char if char in subset_set else " " for char in s]).split()
            
            for segment in segments:
                
                if len(subset) == 1:
                    max_len = max(max_len, len(segment))
                    continue
                    
                # For subsets of size 2 or 3, use prefix differences
                counts = {char: 0 for char in subset}
                # Initial state: all differences are 0 at index -1
                tracker = {tuple([0] * (len(subset) - 1)): -1}
                
                for idx, char in enumerate(segment):
                    counts[char] += 1
                
                    diffs = []
                    for k in range(1, len(subset)):
                        diffs.append(counts[subset[k]] - counts[subset[0]])
                    
                    key = tuple(diffs)
                    if key in tracker:
                        max_len = max(max_len, idx - tracker[key])
                    else:
                        tracker[key] = idx
                        
        return max_len