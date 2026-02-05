class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        new_array=[]
        n=len(nums)
        for i in range(n):
            a=nums[i]
        
            if a !=0:
                new_array.append(nums[((i+a)%n)])
            else:
                 new_array.append(nums[i])

        return new_array