class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        dp_end = [-float('inf')] * n
       
        curr_inc = -float('inf')
        for i in range(1, n):
            if nums[i] > nums[i-1]:
               
                curr_inc = max(nums[i-1] + nums[i], curr_inc + nums[i])
                dp_end[i] = curr_inc
            else:
                curr_inc = -float('inf')

        dp_start = [-float('inf')] * n
        curr_inc = -float('inf')
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i+1]:
                curr_inc = max(nums[i] + nums[i+1], curr_inc + nums[i])
                dp_start[i] = curr_inc
            else:
                curr_inc = -float('inf')

        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i+1] = prefix_sum[i] + nums[i]

        max_sum = -float('inf')
        
       
        for p in range(1, n - 2):
            if dp_end[p] == -float('inf'):
                continue
            
            for q in range(p + 1, n - 1):
                if nums[q] < nums[q-1]:
                    if dp_start[q] != -float('inf'):
                        
                        mid_sum = prefix_sum[q] - prefix_sum[p+1]
                        max_sum = max(max_sum, dp_end[p] + mid_sum + dp_start[q])
                else:
                    break
                    
        return int(max_sum)