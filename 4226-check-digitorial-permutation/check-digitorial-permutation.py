class Solution:
    def isDigitorialPermutation(self, n: int) -> bool:
        digitorial_numbers = [1, 2, 145, 40585]
    
   
        n_digits_sorted = sorted(list(str(n)))
        
        for target in digitorial_numbers:
            target_digits_sorted = sorted(list(str(target)))
            
            if n_digits_sorted == target_digits_sorted:
                
                return True
                
        return False
