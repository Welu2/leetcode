class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        t=0  
        l=0
        r=len(nums)-1
        while l < r:
            t=max(t,nums[l]+nums[r])
            r-=1
            l+=1

        return t
        