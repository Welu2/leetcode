class Solution:
    def bitwiseComplement(self, n: int) -> int:
        b= bin(n)[2:]
        ans=[]
        for i in b:
            if i == "0":
                ans.append("1")
            else:
                ans.append("0")
        ans="".join(ans)
        return int(ans,2)