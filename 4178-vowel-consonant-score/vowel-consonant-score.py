class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        c=0
        v=0
        vowel=("a","e",'i', 'o',"u")
        
        for i in s:
            if i in vowel:
                v+=1
            elif i in "qwsdfrtypghjklzxcvbnm" :
                c+=1
        if c != 0 :
            return floor(v / c)
        return c
