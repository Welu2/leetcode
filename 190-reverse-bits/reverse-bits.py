class Solution:
    def reverseBits(self, n: int) -> int:
        ans=bin(n)[2:].zfill(32) 
        return int(ans[::-1],2)