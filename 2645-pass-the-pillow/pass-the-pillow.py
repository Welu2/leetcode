class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        position=1 #position of pillow
        i=1 #time
        j=1 #step
        while i <= time:
            position+=j
            if position == n or position==1:
                j*=-1  

            i+=1
        return position
    
            