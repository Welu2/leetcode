class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        def is_non_decreasing(arr):
            for i in range(len(arr) - 1):
                if arr[i] > arr[i + 1]:
                    return False
            return True

        operations = 0
        
        while not is_non_decreasing(nums):
            min_sum = float('inf')
            min_index = -1
            
            for i in range(len(nums) - 1):
                current_sum = nums[i] + nums[i + 1]
                if current_sum < min_sum:
                    min_sum = current_sum
                    min_index = i
            
            
            nums[min_index] = min_sum
            nums.pop(min_index + 1)
            
            operations += 1
            
        return operations