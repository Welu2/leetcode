class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        bit_no=bin(n)[2:]
        for i in range(1,len(bit_no)):
            if bit_no[i-1] == bit_no[i]:
                return False
        return True 