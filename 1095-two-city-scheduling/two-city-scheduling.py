class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        minCosts=0
        change=[]
        
        for i in range(len(costs)):
            a,b=costs[i][0],costs[i][1]
            change.append([b-a,i])
           
        half=len(change)//2
        change.sort(key=lambda x: x[0])
       
        for i in range (half):
            minCosts+=costs[change[i][1] ][1]
            minCosts+=costs[change[i+half][1] ][0]

        
        
        return minCosts
