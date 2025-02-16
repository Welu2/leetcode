class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        l=0
        r=len(nums)-1
        avg=set()
        while l <r:
            avg.add((nums[l]+nums[r])/2)
            l+=1
            r-=1

        return len(avg)

        