class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        f=nums[0]
        s=sorted(nums[1:])

        return f+s[0]+s[1]