class Solution:
    def printVertically(self, s: str) -> List[str]:
        s.strip()
        a=list(s.split())
        j=0
        b=sorted(a,key=len)
      
        result=[]

        while j <len(b[-1]):
            d=""
            for i in range(len(a)):
                if j >=len(a[i]):
                    d+=" "
                else:
                    d+=a[i][j]
          
            result.append(d)
            j+=1
        

        return [j.rstrip() for j in result]
        

