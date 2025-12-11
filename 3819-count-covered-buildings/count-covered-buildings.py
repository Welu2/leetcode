class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        x_groups = defaultdict(list)
        y_groups = defaultdict(list)
        
        for x, y in buildings:
            x_groups[x].append(y)
            y_groups[y].append(x)
        
       
        for x in x_groups:
            x_groups[x].sort()
        for y in y_groups:
            y_groups[y].sort()
        
        covered = 0
        for x, y in buildings:
            y_list = x_groups[x]
            x_list = y_groups[y]
            
            
            if y != y_list[0] and y != y_list[-1] and x != x_list[0] and x != x_list[-1]:
                covered += 1
        
        return covered