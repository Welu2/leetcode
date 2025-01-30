class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        a=num-3 
        if a % 3 ==0:
            b=a//3
            return[b,b+1,b+2]
        return []
