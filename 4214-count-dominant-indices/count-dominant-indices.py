class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        t=sum(nums)
        c=0
        n=len(nums)-1
        for i in range(len(nums)-1):
            t-=nums[i]
            a=(t)/n
            if nums[i] >a:
                c+=1
            n-=1
        return c