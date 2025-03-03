class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) -1
        l=goal - 1
        while l >= 0:   
            if (goal-l) <= nums[l]:
                goal=l
            l-=1

        return goal == 0