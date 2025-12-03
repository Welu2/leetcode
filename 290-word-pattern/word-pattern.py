class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d={}
       
        g=s.split(" ")
        
        d[pattern[0]] = g[0]
        if len(pattern) != len(g):
            return False
        else:
            for j in range(len(pattern)):
                if pattern[j] in d:
                    if d[pattern[j]] != g[j]:
                        
                        return False
                else:
                    d[pattern[j]] = g[j]
        ans=[]
        for i in d:
            ans.append(d[i])
        return True if len(set(ans)) == len(d) else False
