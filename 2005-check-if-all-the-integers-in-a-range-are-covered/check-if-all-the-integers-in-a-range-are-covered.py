class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        values=set()
     
        for i in range(len(ranges)):
            for j in range(ranges[i][0],ranges[i][1]+1):
               if left <= j <= right:
                values.add(j)

        if len(values) == (right+1 -left):
            return True
        return False

            