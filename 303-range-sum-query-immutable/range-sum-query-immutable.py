class NumArray:

    def __init__(self, nums: List[int]):
        self.nums=nums
        self.pnums=[0]*len(nums)
        acc=0
        for i in range(len(self.pnums)):
            acc+=self.nums[i]
            self.pnums[i]=acc
        

    def sumRange(self, left: int, right: int) -> int:
        
        if left==0:
            return self.pnums[right]
        else:
            return self.pnums[right]-self.pnums[left-1]
        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)