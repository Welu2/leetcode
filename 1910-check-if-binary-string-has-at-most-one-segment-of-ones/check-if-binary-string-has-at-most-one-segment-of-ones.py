class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        n=len(s)
        c=1
        i=1
        if n == 1:
            return True
        while i < n:
          
            while i < n and s[i] == "1" :
                i +=1
            if i+1 < n and s[i] == "0" and s[i+1] == "1":
                c+=1
            i+=1
                
        return True if c==1  else False