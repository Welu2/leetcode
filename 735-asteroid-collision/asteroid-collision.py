class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for i in asteroids:
            if i > 0:
                stack.append(i)
            else:
                while stack and stack[-1] > 0:
                    if abs(stack[-1]) < abs(i):
                        stack.pop()
                    elif stack[-1]== -i:
                        stack.pop()
                        break
                    else:
                        break
                else:
                    stack.append(i)
        return stack
