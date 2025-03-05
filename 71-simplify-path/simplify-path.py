class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        paths=path.split('/')
   
        for i in paths:
          
            if i == '' or i == '/' or i == '.':
                continue
            elif  i != '..' :
                stack.append(i)
        
            elif i == '..' and stack:
                    stack.pop()
         
        
        return "/"+"/".join(stack)