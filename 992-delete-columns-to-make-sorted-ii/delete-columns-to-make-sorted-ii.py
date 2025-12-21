class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])
    
        sorted_pairs = [False] * (n - 1)
        deletions = 0

        for j in range(m):  
            
            must_delete = False
            for i in range(n - 1):
                if not sorted_pairs[i] and strs[i][j] > strs[i+1][j]:
                    must_delete = True
                    break
            
            if must_delete:
                deletions += 1
            else:
                
                for i in range(n - 1):
                    if not sorted_pairs[i] and strs[i][j] < strs[i+1][j]:
                        sorted_pairs[i] = True
        
        return deletions