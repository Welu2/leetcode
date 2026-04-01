class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n= len(positions)
    
        indices = sorted(range(n), key=lambda i: positions[i])
        stack = [] # Stores indices of robots moving Right ('R')
        
        for i in indices:
            if directions[i] == 'R':
                stack.append(i)
            else:
                
                while stack and healths[i] > 0:
                    top = stack[-1]
                    if healths[i] > healths[top]:
                        # Left robot wins, Right robot destroyed
                        healths[i] -= 1
                        healths[top] = 0
                        stack.pop()
                    elif healths[i] < healths[top]:
                        # Right robot wins, Left robot destroyed
                        healths[top] -= 1
                        healths[i] = 0
                    else:
                        # Both destroyed
                        healths[i] = 0
                        healths[top] = 0
                        stack.pop()
                        
        # Return healths of survivors in their original input order
        return [h for h in healths if h > 0]
            