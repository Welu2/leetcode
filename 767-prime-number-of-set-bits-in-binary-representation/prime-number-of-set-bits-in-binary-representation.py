class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        count=0
        d=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
        for i in range(left,right+1):
            b=bin(i)[2:]
            if b.count("1") in d:
                count+=1
        return count