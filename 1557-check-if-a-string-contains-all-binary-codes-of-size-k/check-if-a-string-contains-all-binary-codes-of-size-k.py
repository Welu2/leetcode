class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        required_count = 1 << k
        # Set to store unique substrings found
        found_codes = set()
        
        # Iterate through s with a window of size k
        for i in range(len(s) - k + 1):
            substring = s[i : i + k]
            found_codes.add(substring)
            
            
            if len(found_codes) == required_count:
                return True
                
        return False