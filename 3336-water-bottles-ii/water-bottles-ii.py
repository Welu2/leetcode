class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        drunk=0
        while numBottles >= numExchange:
            drunk+=numExchange
            numBottles-=numExchange
            numBottles+=1
            numExchange+=1

        return drunk+numBottles