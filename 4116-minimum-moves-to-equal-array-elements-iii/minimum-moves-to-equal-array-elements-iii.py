class Solution:
    def minMoves(self, nums: List[int]) -> int:
        min_v=0
        x=max(nums)
        for i in nums:
            min_v+=(x-i)

        return min_v
        