class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        lost=[matches[j][1] for j in range(len(matches)) ]
        lost=Counter(lost)
        
        win=[]
        
        for i in range(len(matches)):
            
            if matches[i][0] not in lost.keys() and matches[i][0] not in win :
                win.append(matches[i][0])
        loser=[]
        
        for j in lost:
            if lost[j]==1:
                loser.append(j)
        win.sort()
        loser.sort()
        result=[win,loser]
        return result