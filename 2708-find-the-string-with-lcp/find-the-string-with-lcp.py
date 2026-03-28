class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        res = [0] * n
        curr_char = 1
        
        # 1. Greedy Assignment
        for i in range(n):
            if res[i] > 0: continue
            if curr_char > 26: return "" # More than 26 chars needed
            
            for j in range(i, n):
                if lcp[i][j] > 0:
                    res[j] = curr_char
            curr_char += 1

        word = "".join(chr(ord('a') + c - 1) for c in res)

        # 2. Validation
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                
                expected = 0
                if word[i] == word[j]:
                    if i == n - 1 or j == n - 1:
                        expected = 1
                    else:
                        expected = 1 + lcp[i + 1][j + 1]
                
                # Check if provided LCP matches the calculated logic
                if lcp[i][j] != expected:
                    return ""
                    
        return word