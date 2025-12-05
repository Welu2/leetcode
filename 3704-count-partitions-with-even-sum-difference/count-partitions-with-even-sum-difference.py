class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        even=0
        t=sum(nums)
        r=0
        for i,n in enumerate(nums):
            r+=n
            t-=n
            if i< len(nums)-1 and (r-t) % 2 == 0:
                even+=1
          
        return even

        