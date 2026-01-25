class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        m=float("inf")
        nums.sort()
        for j in range(len(nums)-k+1):
            b=nums[j:k+j]
            
            m=min(m,b[-1]-b[0])

        if k == 1:
            m=0

        return m
