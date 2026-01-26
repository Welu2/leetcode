class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
    
        # Initialize minimum difference with the first adjacent pair
        min_diff = arr[1] - arr[0]
        
        # First pass: Find the actual minimum absolute difference
        for i in range(2, len(arr)):
            min_diff = min(min_diff, arr[i] - arr[i-1])
        
        # Second pass: Collect all pairs that have the minimum difference
        result = []
        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] == min_diff:
                result.append([arr[i-1], arr[i]])
                
        return result
