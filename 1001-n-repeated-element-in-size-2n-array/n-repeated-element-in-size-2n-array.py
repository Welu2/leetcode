class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        d=Counter(nums)
        n=len(set(nums))-1
        for j in d:
            if d[j] == n:
                return j