class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        a=1
        total=0
        for j in range(1,len(columnTitle)+1):
            if j ==1:
                total+=(ord(columnTitle[-j]))-64
            else:
                total+=(26**a)*(ord(columnTitle[-j])-64)
                a+=1

        return total