class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        c=0
        t=sum(apple)
        capacity.sort(reverse=True)
        for j in capacity:
            
            if t > 0:
                c+=1
                t-=j
        return c