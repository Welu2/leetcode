class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        d=defaultdict(int)
        s="abcdefghijklmnopqrstuvwxyz"
        for ch in range(len(s)) :
            d[s[ch]]=weights[ch]

        ans=[]
        for j in words:
            t=0
            for i in j:
                t+=d[i]
            t%=26
            ans.append(chr(ord("z")-t))
        return "".join(ans)