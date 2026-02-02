class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        n = len(nums)
       
        target_count = k - 1
        left = SortedList()  
        right = SortedList() #
        current_sum = 0
        
        def add(val):
            nonlocal current_sum
            left.add(val)
            current_sum += val
           
            if len(left) > target_count:
                largest_in_left = left.pop(-1)
                current_sum -= largest_in_left
                right.add(largest_in_left)
                
        def remove(val):
            nonlocal current_sum
           
            if val in left and (not right or val <= left[-1]):
                left.remove(val)
                current_sum -= val
               
                if right:
                    smallest_in_right = right.pop(0)
                    left.add(smallest_in_right)
                    current_sum += smallest_in_right
            else:
                right.remove(val)

       
        for i in range(1, min(dist + 2, n)):
            add(nums[i])
            
        min_total_cost = current_sum
        
        
        for i in range(dist + 2, n):
           
            add(nums[i])
           
            remove(nums[i - dist - 1])
            
            min_total_cost = min(min_total_cost, current_sum)
            
        return nums[0] + min_total_cost