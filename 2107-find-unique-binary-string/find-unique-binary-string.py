class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n=len(nums)
        nums_set = set(nums)
    
        def backtrack(current):
            
            if len(current) == n:
                if current not in nums_set:
                    return current
                return None
            
            
            for char in ["0", "1"]:
                res = backtrack(current + char)
                if res: 
                    return res
            
            return None

        return backtrack("")

        