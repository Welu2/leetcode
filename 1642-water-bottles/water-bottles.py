class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        b=0
        while numBottles >= numExchange:
            numBottles-=numExchange
            numBottles+=1
            b+=numExchange

        return numBottles+b