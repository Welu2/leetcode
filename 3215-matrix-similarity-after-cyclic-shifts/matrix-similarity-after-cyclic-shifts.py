class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m = len(mat)
        n = len(mat[0])
        
        shift = k % n
        
        for i in range(m):
            row = mat[i]
            
            if i % 2 == 0:
              
                shifted_row = row[shift:] + row[:shift]
            else:
               
                shifted_row = row[-shift:] + row[:-shift] if shift != 0 else row
            
            if row != shifted_row:
                return False
                
        return True