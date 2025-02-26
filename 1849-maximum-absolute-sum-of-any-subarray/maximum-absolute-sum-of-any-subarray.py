class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        cur=nums[0]
        maxV=nums[0]
        for i in range(1,len(nums)):
            cur+=nums[i]
            cur=max(cur,nums[i])
            maxV=max(maxV,cur)

        cur=nums[0]
        minV=nums[0]
        for i in range(1,len(nums)):
            cur+=nums[i]
       
            cur=min(cur,nums[i])
            minV=min(minV,cur)

        return max(maxV,abs(minV))

